import boto3


def delete_widget(path, bucket):
    s3 = boto3.resource('s3')
    s3.Object(bucket, path).delete()
