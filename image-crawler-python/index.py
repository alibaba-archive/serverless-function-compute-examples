# coding=utf-8
'''
    A demo of a web image crawler that grabs all jpg files from a URL provided by the user and stores them in OSS.
    For example：invk crawler_image -s "{\"url\":\"http://www.xxxx.com\"}"
    Please replace <' var '> with real value
'''

import re
import urllib
import json
import datetime
import oss2
import logging


# The main function
def handler(event, context):
    logger = logging.getLogger()
    evt = json.loads(event)
    url = evt['url']
    logger.info('process url: ' + url)
    endpoint = 'oss-cn-'<region>'.aliyuncs.com' # replace '<region>' with oss bucket region
    creds = context.credentials
    auth = oss2.StsAuth(creds.accessKeyId, creds.accessKeySecret, creds.securityToken)
    bucket = oss2.Bucket(auth, endpoint, '<bucket>') # replace '<bucket>' with oss bucket name

    html = getHtml(url)
    img_list = getImg(html)
    count = 0
    for item in img_list:
        count += 1
        logging.info('fetch and upload image: ' + item)
        # fetch each picture
        pic = urllib.urlopen(item)
        # Store the picture in oss bucket, keyed by timestamp in microsecond unit
        bucket.put_object(str(datetime.datetime.now().microsecond) + '.jpg', pic)

    return 'download success, total pictures:' + str(count)


# Parse urls from content
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


# Get jpg list
def getImg(html):
    reg = r'http:\/\/[^\s,"]*\.png'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist