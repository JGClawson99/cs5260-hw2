import argparse
import boto3

from requests import build_create_request
from s3.upload_widget import upload_widget


def start(rb):
    owner = boto3.client('sts').get_caller_identity().get('Account')

    while True:
        widget_request = build_create_request(owner)
        upload_widget(widget_request, rb)


parser = argparse.ArgumentParser()
parser.add_argument("-rb", "--request-bucket", type=str, help="Request Bucket name")

args, leftovers = parser.parse_known_args()

if __name__ == '__main__':
    start(args.request_bucket)
