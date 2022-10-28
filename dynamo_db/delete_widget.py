import boto3


def delete_widget(widgetId, table):
    db = boto3.resource("dynamodb")
    table = db.Table(table)

    table.delete_item(
        Key={
            "id": widgetId
        }
    )
