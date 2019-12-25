import json
from api.parser.slack import SlackParser
from api.formatter.slack import slack_formatter, slack_test_formatter
from botocore.vendored import requests

def handler(event, context):
    print(event)
    data = SlackParser().parse(event)
    print(data)
    # requests.post("")
    requests.post(data['response_url'],
        headers={
            "Content-Type":"Application/json"
        },
        data=json.dumps(
            {
                "replace_original":True,
                "delete_original":True
            }
        )
    )
    return {
        'statusCode': 200,
        'body': json.dumps({})
    }

    # https://hooks.slack.com/actions/TKK8D3N9Z/888038688582/R2gjlW4kWzEqxZ4c5yRMl2Z4 -H "Content-type:Application/json" -d ''
    # 