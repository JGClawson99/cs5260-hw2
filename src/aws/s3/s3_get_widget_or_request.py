import boto3
import json

s3 = boto3.client('s3')
owner = boto3.client('sts').get_caller_identity().get('Account')


def s3_get_widget_or_request(bucket, key):
    request = s3.get_object(Bucket=bucket, Key=key)
    if request['Body'] is None:
        return {}

    return json.loads(request['Body'].read())
