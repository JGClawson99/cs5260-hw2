import boto3
import json


def get_widget(marker, bucket):
    objects = boto3.client('s3').list_objects(Bucket=bucket, Marker=marker, MaxKeys=1)
    if 'Contents' not in objects:
        return False
    key = objects["Contents"][0]["Key"]
    request = boto3.client('s3').get_object(Bucket=bucket, Key=key)['Body'].read()
    return json.loads(request)
