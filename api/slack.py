import random
import json
from api.parser.slack import SlackParser
from api.formatter.slack import slack_formatter
from api.crawler.aws import news
from api.data.eat import EAT_LIST, TEST_LIST

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
        text = test['problem'] + '\n'
        description = 'No description'
        counter = 1

        for item in test['choices']:
            text = text + str(counter) + '. ' + item + '\n'
            counter = counter + 1

        if test['description']:
            description = test['description']

        return {
            'statusCode': 200,
            'body': json.dumps({
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": text
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Show answer"
                            },
                            "confirm":{
                                "title":{
                                    "type":"plain_text",
                                    "text": 'Answer is ' + str(test['answer'])
                                },
                                "text":{
                                    "type":"plain_text",
                                    "text": description
                                }
                            }
                        }
                    }
                ]
            })
        }