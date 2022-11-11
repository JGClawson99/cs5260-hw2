
from aws.s3 import S3
from aws.dynamo_db import DynamoDB
from aws.sqs import SQS
import json
from requests import build_db_create_request

class RequestHandler:
    def __init__(self, rb=None, rq=None, wdt=None, wb=None):
        self.rb = rb
        self.rq = rq
        self.wdt = wdt
        self.wb = wb
        self.s3 = S3()
        self.db = DynamoDB()
        self.sqs = SQS()

    def upload_widget_request(self, request):
        if self.rb:
            self.s3.put_object(json.loads(request))
        elif self.rq:
            self.sqs.upload_widget_request(self.rq, request)

    def get_widget_requests(self, marker=""):
        if self.rb:
            return self.s3.list_objects(self.rb, marker=marker)
        elif self.rq:
            return self.sqs.get_widget_requests(self.rq)

    def process_request(self, request):
        if self.wb:
            return self.s3.put_object(json.loads(request))
        elif self.wdt:
            return self.db.put_item(self.wdt, request)
