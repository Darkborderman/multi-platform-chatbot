def slack_formatter(data:dict):
    
    return {
        'text': f'*{data["title"]}*\n {data["description"]}\n {data["URL"]}',
        'mrkdwn': True
    }

def slack_test_formatter(data:dict):
    text = data['problem'] + '\n'
    description = 'No description'
    counter = 1

    for item in data['choices']:
        text = text + str(counter) + '. ' + item + '\n'
        counter = counter + 1

    if data['description']:
        description = data['description']
    
    return {
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': text
                },
                'accessory': {
                    'type': 'button',
                    'text': {
                        'type': 'plain_text',
                        'text': 'Show answer'
                    },
                    'confirm':{
                        'title':{
                            'type':'plain_text',
                            'text': 'Answer is ' + data['answer']
                        },
                        'text':{
                            'type':'plain_text',
                            'text': description
                        }
                    }
                }
            }
        ]
    }