import boto3


s3 = boto3.client('s3')

def s3_list_widgets_or_requests(bucket, marker):
    request = s3.list_objects(Bucket=bucket, Marker=marker)

    if 'Contents' not in request:
        return []

    return request['Contents']

# widgets = list_widgets('usu-cs5260-smart-requests', 'widgets/')
# widget = get_widget('usu-cs5260-smart-requests', widgets[0]['Key'])
# print(widget)