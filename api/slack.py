import random
import json
from api.parser.slack import SlackParser
from api.formatter.slack import slack_formatter, slack_test_formatter
from api.crawler.aws import news
from api.data.eat import EAT_LIST
from api.data.test import TEST_LIST

def handler(event, context):
    print(event)
    data = SlackParser().parse(event)
    print(data)
    response = {}
    if data['command'] == '/eat':
        eat = random.choice(EAT_LIST)
        response = slack_formatter(eat)
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    if data['command'] == '/test':

        test = random.choice(TEST_LIST)
        response = slack_test_formatter(test)
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }