import uuid



def build_update_request(widgetId, owner):
    return {
        "type": "update",
        "id": widgetId,
        "requestId": str(uuid.uuid1()),
        "owner": owner
    }




def build_create_request(owner):
    return {
        "type": "create",
        "id": str(uuid.uuid1()),
        "requestId": str(uuid.uuid1()),
        "owner": owner
    }