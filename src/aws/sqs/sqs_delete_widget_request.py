import boto3

sqs = boto3.client('sqs')


def sqs_delete_widget_request(queue_url, receipt_handle):
    return sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
