import json
from botocore.vendored import requests


def news(event, context):

    try:
        page = event['page']
    except:
        page = 0
        print('automatically use page 0')

    res = requests.get(f'https://aws.amazon.com/api/dirs/items/search?item.directoryId=whats-new&sort_by=item.additionalFields.postDateTime&sort_order=desc&size=20&item.locale=en_US&page={page}')
    res_json = res.json()

    resp = []
    for article in res_json['items']:
        resp.append({
            'title':article["item"]["additionalFields"]["headline"],
            'url': f'https://aws.amazon.com{article["item"]["name"]}',
            'description':article["item"]["dateUpdated"]
        })

    response = {
        "statusCode": 200,
        "body": json.dumps(resp)
    }

    return response
