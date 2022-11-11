import boto3
import json

s3 = boto3.resource('s3')
owner = boto3.client('sts').get_caller_identity().get('Account')


def s3_put_widget_or_request(bucket, widget_or_request):
    bucket = s3.Bucket(bucket)
    
    request = bucket.put_object(Body=bytes(json.dumps(widget_or_request).encode('UTF-8')), Key=f'widgets/{owner}/{widget_or_request["id"]}')
    return request
