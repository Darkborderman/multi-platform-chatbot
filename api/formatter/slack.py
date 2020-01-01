def slack_formatter(data: dict):

    return {
        'text': f'*{data["title"]}*\n {data["description"]}\n {data["URL"]}',
        'mrkdwn': True
    }

def slack_test_formatter(data: dict):
    # append question text
    text = data['problem'] + '\n'
    counter = 1
    for item in data['options']:
        text = text + str(counter) + '. ' + item + '\n'
        counter = counter + 1

    # append result
    answer = 'Answer is '
    for item in data['answers']:
        answer = answer + item + ' '

    description = ''
    if not data['description']:
        description += 'No description'
    else:
        description += data['description']

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
                            'text': answer
                        },
                        'text':{
                            'type':'plain_text',
                            'text': description
                        },
                        'confirm':{
                           'type':'plain_text',
                            'text':'Okay, burn it'
                        }
                    }
                }
            }
        ]
    }
