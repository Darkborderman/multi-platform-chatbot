import json

def lambda_handler(event, context):
    print(json.dumps(event,indent=4))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
