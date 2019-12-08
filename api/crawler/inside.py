import json
from botocore.vendored import requests
from python.shared import BeautifulSoup

def news(event, context):

    result = requests.get('https://www.inside.com.tw/?page=1')

    html = result.text

    soup = BeautifulSoup(html, 'html.parser')

    # delete special div in index
    if soup.find('div',class_='Independent_study'):
        soup.find('div',class_='Independent_study').decompose()

    if soup.find('div',class_='Independent_study_down'):
        soup.find('div',class_='Independent_study_down').decompose()

    posts = soup.find_all('div',class_='post_list_item')
    resp=[]

    for item in posts:
        # print(item)
        obj = item.find('a', class_='js-auto_break_title')
        if not isinstance(obj,type(None)):
            resp.append({
                'title':item.find('a', class_='js-auto_break_title').text,
                'url': item.find('a', class_='js-auto_break_title')['href'],
                'description':item.find('p', class_='post_description').text
            })

    response = {
        "statusCode": 200,
        "body": json.dumps(resp)
    }

    return response
