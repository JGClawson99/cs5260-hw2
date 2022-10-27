# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import boto3

from dynamo_handler import DynamoHandler


parser = argparse.ArgumentParser()
parser.add_argument("-rb", "--request-bucket", type=str, help="Request Bucket name")
parser.add_argument("-wb", "--web-bucket", type=str, help="Web Bucket name")
parser.add_argument("-dwt", "--dynamo-widget-table", help="DynamoDB Widget Table Name")

args = parser.parse_args()


account_id = boto3.client('sts').get_caller_identity().get('Account')
print(account_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello world")
    # dynamo.widget_create_request()
    # if args.test:
    #     print("haha")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
