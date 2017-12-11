# -*- coding=utf-8
import os
import sys
import time

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError

# 腾讯云COSV5Python SDK, 目前可以支持Python2.6与Python2.7

app_id = ''     # 替换为用户的app_id
secret_id = ''     # 替换为用户的secret_id
secret_key = ''     # 替换为用户的secret_key
region = 'ap-shanghai'    # 替换为用户的region
token = ''                 # 使用临时秘钥需要传入Token，默认为空,可不填
config = CosConfig(Appid=app_id, Region=region, Access_id=secret_id, Access_key=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)

# 文件流 简单上传
file_name = "%s_%s" % (os.path.basename(sys.argv[1]), int(time.time()))
with open(sys.argv[1], 'rb') as fp:
    response = client.put_object(
        Bucket='uploads',
        Body=fp,
        Key=file_name,
        StorageClass='STANDARD',
        CacheControl='no-cache',
        ContentDisposition=file_name
    )

    if response.get('Etag'):
    	url = 'http://uploads-%s.cossh.myqcloud.com/%s' % (app_id, file_name)
    	sys.stdout.write(url)
