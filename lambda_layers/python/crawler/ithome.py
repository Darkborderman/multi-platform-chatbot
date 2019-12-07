import json
from botocore.vendored import requests
from python.shared import BeautifulSoup


def news(event, context):

    result = requests.get('https://www.ithome.com.tw/news?page=0')
    html = result.text
    soup = BeautifulSoup(html, 'html.parser')

    resp=[]

    posts = soup.find_all('div',class_='span4 channel-item')

    for item in posts:
        title = item.find('p', class_='title')
        url = title.a['href']
        title = title.a.text
        obj = item.find('a', class_='js-auto_break_title')
        resp.append({
            'title': title,
            'url': f'https://www.ithome.com.tw{url}',
            'description': item.find('div', class_='summary').text
        })

    posts = soup.find_all('div',class_='span4 channel-item no-margin-left')

    for item in posts:
        title = item.find('p', class_='title')
        url = title.a['href']
        title = title.a.text
        obj = item.find('a', class_='js-auto_break_title')
        resp.append({
            'title': title,
            'url': f'https://www.ithome.com.tw{url}',
            'description': item.find('div', class_='summary').text
        })
    
    response = {
        "statusCode": 200,
        "body": json.dumps(resp)
    }

    return response
