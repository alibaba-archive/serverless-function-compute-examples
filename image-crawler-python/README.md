#Fetch image from URL then upload to Aliyun OSS Example
This example demonstrates how to fetch an image from a remote web source and upload this image to an OSS bucket using the serverless framework with alibaba cloud as the provider.

## Setup

* Install Serverless CLI v1.26.1+. You can get it by running `npm i -g serverless`.
* Apply for an Alibaba cloud account and apply to use [Aliyun Function Compute](https://fc.console.aliyun.com) service
* Enable [Aliyun OSS service](https://oss.console.aliyun.com) and create a bucket in the same region

### Install demo & `serverless-aliyun-function-compute` plugin
You can install the demo from GitHub:

```sh
serverless install --url https://github.com/aliyun/serverless-function-compute-examples/tree/master/image-crawler-python
```

The structure of the project should look something like this:

```
├── index.py
├── package.json
└── serverless.yml
```

Install the latest `serverless-aliyun-function-compute` plugin to your service from https://github.com/aliyun/serverless-aliyun-function-compute

```sh
serverless plugin install --name serverless-aliyun-function-compute
```

### Prepare a credential file
In order to deploy this function, we need the credentials with permissions to access Aliyun Function Compute.
Please create a `credentials` file and configure the credentials in it.
Here is an example `credentials` file:

```ini
[default]
aliyun_access_key_id = xxxxxxxx
aliyun_access_key_secret = xxxxxxxxxxxxxxxxxxxx
aliyun_account_id = 1234567890
```

* You can find the `aliyun_access_key_secret` and `aliyun_access_key_id` from [AccessKey](https://ak-console.aliyun.com/?#/accesskey). You can also choose to create an Access Key or use sub-account Access Key.
* You can find the `aliyun_account_id` from [Account](https://account-intl.console.aliyun.com/?#/secure).
* After creating the `aliyun_credentials` file, please make sure to change the `credentials` field value in `serverless.yml` to the absolute file path.

### Fill in your OSS bucket info

* replace '<region>' with oss bucket region in the index.py file
* replace '<bucket>' with oss bucket name in the index.py file

For example, if your bucket domain name is "demo.oss-us-east-1.aliyuncs.com", "us-east-1" is the region, "demo" is the bucket name.

### Prepare input file

Please create a `event.json` file and copy the following content.
```json
{
  "url": "https://www.wsj.com"
}
```

## Deploy and invoke
Make sure that you have activated Function Compute before attempting to deploy your function.

* Deploy your service to Aliyun:

  ```sh
  serverless deploy
  ```

* Invoke a function directly:

  ```sh
  serverless invoke --function image-crawler --path event.json
  ```