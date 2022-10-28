'''
    You must replace <FMI_1> with the table name FoodProducts
    You must replace <FMI_2> with a product name. apple pie
    You must replace <FMI_3> with a444
    You must replace <FMI_4> with 595
    You must replace <FMI_5> with the description: It is amazing!
    You must replace <FMI_6> with a tag: whole pie
    You must replace <FMI_7> with a tag: apple
'''

import boto3
from botocore.exceptions import ClientError


def conditional_put(item, dwt, conditional_expression=""):
    db = boto3.resource("dynamodb").Table(dwt)

    try:
        response = db.put_item(
            TableName=dwt,
            Item=item,
            # ConditionExpression=conditional_expression
        )
    except ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise


"""
Copyright @2021 [Amazon Web Services] [AWS]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Modified by Jacob Clawson
"""
