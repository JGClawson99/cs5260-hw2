import argparse

import boto3

from aws.s3.s3_list_widgets_or_requests import s3_list_widgets_or_requests
from aws.s3.s3_get_widget_or_request import s3_get_widget_or_request
from aws.s3.s3_put_widget_or_request import s3_put_widget_or_request
from aws.s3.s3_delete_widget_or_request import s3_delete_widget_or_request
from aws.sqs.sqs_receive_widget_requests import sqs_receive_widget_requests
from aws.dynamo_db.dynamodb_put_widget import dynamodb_put_widget
from aws.sqs.sqs_delete_widget_request import sqs_delete_widget_request
import json

owner = boto3.client('sts').get_caller_identity().get('Account')
sqs_ready_to_delete = []

def get_widget_requests(rb=None, rq=None):
    widget_requests = []
    if rb is not None:
        widget_requests_info_list = s3_list_widgets_or_requests(rb, f'widgets/{owner}')
        for widget_request_info in widget_requests_info_list:
            widget_requests.append(s3_get_widget_or_request(rb, widget_request_info['Key']))
        return widget_requests
    if rq is not None:
        widget_requests_info_list = sqs_receive_widget_requests(rq)
        for widget_request_info in widget_requests_info_list:
            widget_requests.append(json.loads(widget_request_info['Body']))
            sqs_ready_to_delete.append(widget_request_info['ReceiptHandle'])
        return widget_requests

def get_widget(widget_request, wdt=None, wb=None):
    if wb is not None:
        return s3_get_widget_or_request(wb, widget_request['id'])

def create_widget(widget_request, wdt=None, wb=None):
    del widget_request['type']
    del widget_request['requestId']
    if wb is not None:
        return s3_put_widget_or_request(wb, widget_request)
    if wdt is not None:
        return dynamodb_put_widget(widget_request)
        
def delete_widget(widget, wdt=None, wb=None):
    if wb is not None:
        s3_delete_widget_or_request(wb, widget['id'])

def delete_widget_request(widget_request, rb=None, rq=None):
    if rb is not None:
        s3_delete_widget_or_request(rb, widget_request)
    if rq is not None:
        for rh in sqs_ready_to_delete:
            sqs_delete_widget_request(rq, rh)
        sqs_ready_to_delete.clear()

def process_widget_request(widget_request=None, wdt=None, wb=None, dwt=None):
    widget = None
    request_type = widget_request['type']
    if request_type == 'update':
        widget = get_widget(widget_request, wdt=wdt, wb=wb)
    elif request_type == 'create':
        create_widget(widget_request=widget_request, wdt=wdt, wb=wb)
    elif request_type == 'delete':
        widget = get_widget(widget_request, wdt=wdt, wb=wb)
        delete_widget(widget=widget, wdt=wdt, wb=wb)
    print("widget request " + widget_request['id'] + " proccessed")

def start(rb=None, rq=None, wdt=None, wb=None, dwt=None):
    while True:
        print("getting widget requests ...")
        widget_requests = get_widget_requests(rb=rb, rq=rq)
        for widget_request in widget_requests:
            process_widget_request(widget_request=widget_request, wdt=wdt, dwt=dwt, wb=wb)
            delete_widget_request(widget_request, rb=rb, rq=rq)

parser = argparse.ArgumentParser()
parser.add_argument("-rb", "--request-bucket", type=str, help="Request Bucket name")
parser.add_argument("-wb", "--web-bucket", type=str, help="Web Bucket name")
parser.add_argument("-dwt", "--dynamo-widget-table", help="DynamoDB Widget Table Name")
parser.add_argument("-rq", "--sqs", help="Simple Queue Service Url")

args, leftovers = parser.parse_known_args()

if __name__ == '__main__':
    start(args.request_bucket, wb=args.web_bucket, dwt=args.dynamo_widget_table, rq=args.sqs)
