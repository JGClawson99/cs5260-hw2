import boto3
from dynamo_db.conditional_put_widget import conditional_put
from dynamo_db.delete_widget import delete_widget

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

# It would be nice to isolate test cases so functions like conditional_put
# aren't used in other test cases. This should work for this assignment.
def test_delete_widget():
    widget = {
        "owner": "some owner",
        "id": "some id"
    }
    conditional_put(widget, "widgets")
    delete_widget("some id", "widgets")

    table = boto3.resource("dynamodb").Table("widgets")
    response = table.get_item(Key={
        "id": "some id"
    })

    if "Item" in response:
        assert False
    else:
        assert True


test_conditional_put_widget()
test_delete_widget()
