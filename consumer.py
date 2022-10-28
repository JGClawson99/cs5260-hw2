import argparse

import boto3

from s3.get_widget import get_widget
from s3.upload_widget import upload_widget
from s3.delete_widget import delete_widget
from dynamo_db.conditional_put_widget import conditional_put


def start(bucket, wb=None, dwt=None):
    owner = boto3.client('sts').get_caller_identity().get('Account')

    while True:
        widget_request = get_widget(f'widgets/{owner}', bucket)
        if widget_request:
            print(widget_request)
            del widget_request['type']
            del widget_request['requestId']
            if wb is not None:
                upload_widget(widget_request, wb)
            else:
                conditional_put(widget_request, dwt, 'attribute_not_exists(id)')
            delete_widget(f'widgets/{owner}/{widget_request["id"]}', bucket)


parser = argparse.ArgumentParser()
parser.add_argument("-rb", "--request-bucket", type=str, help="Request Bucket name")
parser.add_argument("-wb", "--web-bucket", type=str, help="Web Bucket name")
parser.add_argument("-dwt", "--dynamo-widget-table", help="DynamoDB Widget Table Name")

args, leftovers = parser.parse_known_args()


if __name__ == '__main__':
    start(args.request_bucket, wb=args.web_bucket, dwt=args.dynamo_widget_table)
