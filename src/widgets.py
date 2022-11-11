

def process_request(widget_request):
    type = widget_request['type']
    if type == "create":
        return process_create_request(widget_request)

def process_create_request(widget_request):
    if widget_request['type'] is not None:
        del widget_request['type']
    if widget_request['requestId'] is not None:
        del widget_request['requestId']

    return widget_request