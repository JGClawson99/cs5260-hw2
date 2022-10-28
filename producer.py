import argparse
import boto3

from requests import build_create_request
from s3.upload_widget import upload_widget
import logging

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('producer.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)


def start(rb):
    owner = boto3.client('sts').get_caller_identity().get('Account')

    while True:
        widget_request = build_create_request(owner)
        key = upload_widget(widget_request, rb)
        logger.log(level=logging.INFO, msg="request created " + key)
        print("request created " + key)

parser = argparse.ArgumentParser()
parser.add_argument("-rb", "--request-bucket", type=str, help="Request Bucket name")

args, leftovers = parser.parse_known_args()

if __name__ == '__main__':
    start(args.request_bucket)
