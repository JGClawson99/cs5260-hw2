import boto3

s3 = boto3.client('s3')
owner = boto3.client('sts').get_caller_identity().get('Account')

def s3_delete_widget_or_request(bucket, widget_or_request):
    request = s3.delete_object(Bucket=bucket, Key=f'widgets/{owner}/{widget_or_request["id"]}')
    return request
