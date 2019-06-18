import sys
reload(sys)
sys.setdefaultencoding('utf8')

import io
import boto3
import time
from io import BytesIO

cos_endpoint = 'http://192.168.174.101'
cos_access_key_id = 'sAZCqzmZb9H8cP1AtNcy'
cos_secret_key = 'm7N5Xmv9E0Q71PfZmpsT9T8MxhBmTS7YGu5Lu830'
addressing_style = 'path'
signature_version = 's3'
bucket = 'vault1'

session = boto3.session.Session(aws_access_key_id=cos_access_key_id, aws_secret_access_key=cos_secret_key)
s3 = session.resource('s3', endpoint_url=cos_endpoint, verify=False,
                      config=boto3.session.Config(signature_version=signature_version, s3={'addressing_style': addressing_style}))
s3c = session.client('s3', endpoint_url=cos_endpoint, verify=False,
                      config=boto3.session.Config(signature_version=signature_version, s3={'addressing_style': addressing_style}))


s3.Object('vault1', 'upload.py').put(Body='hello world', Metadata={'time': time.asctime()})

resp = s3c.list_objects_v2(Bucket='vault1')
tStart = time.time()
for obj in resp['Contents']:
    print (obj['Key'])
tEnd = time.time()
print "It cost %f sec" % (tEnd - tStart)

tStart = time.time()	
for key in s3c.list_objects(Bucket='vault1')['Contents']:
    object_summary = s3c.head_object(Bucket='vault1', Key=key['Key'])
    print('Metadata: {}'.format(object_summary.get('Metadata')))
tEnd = time.time()
print "It cost %f sec" % (tEnd - tStart)
