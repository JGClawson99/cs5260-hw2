import boto3

import json


class S3Handler:
    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.rb = "usu-cs5260-smart-requests"
        self.dist = "usu-cs5260-smart-dist"

    def create_widget(self, widget):
        with open("widgets-owner-widgetId.txt", "w+") as file:
            file.write(json.dumps(widget))
            file.seek(0, 0)
            self.s3.Bucket(self.rb).upload_file(file.name, f'widgets/owner/widgetId.json')
            file.close()

    def delete_widget(self, widget):
        self.s3.Object(self.rb, "widgets/owner/widgetId.json").delete()
