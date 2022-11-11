import boto3

sqs = boto3.client('sqs')

def sqs_receive_widget_requests(queue_url):
    request = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)

    if not "Messages" in request:
        return []
        
    return request['Messages']