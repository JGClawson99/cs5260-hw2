import boto3


class DynamoHandler:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table("widgets")

    def create_widget(self, request):
        self.table.put_item(
            Item=request
        )

    def delete_widget(self, widgetId):
        self.delete_item(
            Key={
                "id": widgetId
            }
        )

    # def update_widget(request):
