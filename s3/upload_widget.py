# def upload_file(self, data, path):
#     with open("file", "w+") as file:
#         file.write(json.dumps(data))
#         file.seek(0, 0)
#         self.s3.Bucket(self.bucket).upload_file(file.name, path)
#         file.close()

import logging
import boto3
from botocore.exceptions import ClientError
import os
import json
import boto3


def upload_widget(widget_data, bucket):
    owner = boto3.client('sts').get_caller_identity().get('Account')

    with open("file", "w+") as file:
        file.write(json.dumps(widget_data))
        file.seek(0, 0)
        boto3.resource('s3').Bucket(bucket).upload_file(file.name, f'widgets/{owner}/{widget_data["id"]}')
        file.close()

    return f'widgets/{owner}/{widget_data["id"]}'