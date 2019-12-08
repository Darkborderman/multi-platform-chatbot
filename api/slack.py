import random
import json
from parser.slack import SlackParser
from formatter.slack import slack_formatter
from crawler.aws import news
from data.eat import EAT_LIST

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
