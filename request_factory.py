import uuid


class RequestFactory:
    def __init__(self, owner):
        self.owner = owner

    def update(self, widgetId):
        return {
            "type": "update",
            "widgetId": widgetId,
            "requestId": str(uuid.uuid1()),
            "owner": self.owner
        }

    def create(self):
        return {
            "type": "create",
            "widgetId": str(uuid.uuid1()),
            "requestId": str(uuid.uuid1()),
            "owner": self.owner
        }

    # def update(self):




