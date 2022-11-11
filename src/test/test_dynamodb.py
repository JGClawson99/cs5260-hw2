import boto3

owner = boto3.client('sts').get_caller_identity().get('Account')

from requests import build_create_request
from aws.dynamo_db.dynamodb_put_widget import dynamodb_put_widget

def test_put_widget_or_request()
    request = build_create_request(owner)
    dynamodb_put_widget

def test_conditional_put_widget():
    widget = {
        "owner": "some owner",
        "id": "some id"
    }
    conditional_put(widget, "widgets")

    table = boto3.resource("dynamodb").Table("widgets")
    response = table.get_item(Key={
        "id": "some id"
    })

    if "Item" in response:
        assert True
    else:
        assert False
