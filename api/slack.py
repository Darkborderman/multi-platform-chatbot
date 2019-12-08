import random
import json
from api.parser.slack import SlackParser
from api.formatter.slack import slack_formatter
from api.crawler.aws import news
from api.data.eat import EAT_LIST

def handler(event, context):
    print(event)
    data = SlackParser().parse(event)
    print(data)
    response = {}
    if data['command'][0] == '/eat':
        eat = random.choice(EAT_LIST)
        response = slack_formatter(eat)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
