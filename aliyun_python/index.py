#coding=utf-8
import logging
import urllib, urllib2, sys
import json

def handler(event, context):
    logger = logging.getLogger()
    logger.info('look up weather info for: %s', event)
    evt = json.loads(event)
    city = evt['city'].decode()
    host = 'http://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    # register and get your appcode here: https://market.aliyun.com/products/57126001/cmapi014302.html
    appcode = '<your app code>'
    params = {'city' : city, 'citycode' : 'citycode', 'cityid' : 'cityid', 'ip' : 'ip', 'location' : 'location'}
    queries = urllib.urlencode(params)
    url = host + path + '?' + queries

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        return content