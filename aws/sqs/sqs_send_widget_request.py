import boto3
import json

sqs = boto3.client('sqs')

def sqs_send_widget_request(queue_url, widget_request):
    request = sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(widget_request))
    return request
