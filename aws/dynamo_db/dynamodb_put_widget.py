import boto3
from botocore.exceptions import ClientError

db = boto3.client('dynamodb')

def append_other_attributes(widget, item):
    for attribute in widget['otherAttributes']:
        item['otherAttributes']['L'].append({
            'M': {
                'Name': {'S': attribute['name']},
                'Value': {'S': attribute['value']}
            }
        })
    
    return item

def dynamodb_put_widget(widget):
    item={
        'id': {
            'S': widget['requestId']
        },
        'owner': {
            'S': widget['owner']
        },
        'label': {
            'S': widget['label']
        },
        'description': {
            'S': widget['description']
        },
        'otherAttributes': {
            'L': []
        }
    }
    item = append_other_attributes(widget, item)
    
    response = db.put_item(
        TableName='widgets',
        Item = item
    )

dynamodb_put_widget({"type":"create","requestId":"ecf1f141-a125-4f25-af13-04ec28dd6b44","widgetId":"2b8186fc-11a4-4b97-b048-571fe200e646","owner":"John Jones","label":"V","description":"VKZKAPGESWQYALXNPFOIWGUKDPRFGZCSYPBYIAJLYUMVTAULFIFIMLVGDKZJSRVOVFSYCSCJRMYFZNRMUVINHQRVTVSOOP","otherAttributes":[{"name":"price","value":"6.36"},{"name":"quantity","value":"564"},{"name":"note","value":"IZWAANKACMEEZRUQJSCPRIEUQHLEPAKUAXTQMILEBDMDCTERPHYCLCSCXMBCEFYXFIWVUCLGXSPSUKBVLAPYFOJPJROYCHPF"}]})