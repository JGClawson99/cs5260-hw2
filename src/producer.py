import argparse
import boto3
import os

from aws.sqs.sqs_send_widget_request import sqs_send_widget_request
from requests import build_create_request
from aws.s3.s3_put_widget_or_request import s3_put_widget_or_request

owner = boto3.client('sts').get_caller_identity().get('Account')

def start_with_sqs(queue_url):
    while True:
        widget_request = build_create_request(owner)
        sqs_send_widget_request(queue_url, widget_request)
        print("request sent to queue ...")

def start_with_bucket(rb):
    while True:
        widget_request = build_create_request(owner)
        s3_put_widget_or_request(rb, widget_request)
        print("request sent to bucket")

parser = argparse.ArgumentParser()
parser.add_argument("-rb", "--request-bucket", type=str, help="Request Bucket Url")
parser.add_argument("-rq", "--request-queue", type=str, help="Request Queue Url")

args, leftovers = parser.parse_known_args()

if __name__ == '__main__':
    if args.request_queue is not None:
        start_with_sqs(args.request_queue)
    else:
        start_with_bucket(args.request_bucket)

