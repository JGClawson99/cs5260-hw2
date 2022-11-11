import boto3

from s3.upload_widget import upload_widget
from s3.delete_widget import delete_widget
from s3.get_widget import get_widget


def test_delete_widget():
    widget = {
        "owner": "some owner",
        "id": "some id"
    }

    key = upload_widget(widget, "usu-cs5260-smart-requests")
    delete_widget(key, "usu-cs5260-smart-requests")

    if not get_widget(key, "usu-cs5260-smart-requests"):
        assert True
    else:
        assert False


def test_upload_widget():
    widget = {
        "owner": "some owner",
        "id": "some id"
    }

    key = upload_widget(widget, "usu-cs5260-smart-requests")

    try:
        boto3.client('s3').get_object(Bucket="usu-cs5260-smart-requests", Key=key)
        assert True
    except AssertionError:
        assert False
