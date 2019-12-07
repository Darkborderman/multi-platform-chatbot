from crawler.aws import news

def handler(event, context):
    # TODO implement
    print(event)
    # print(event['body'])
    args = event['body'].split('&')
    request_args={}
    for arg in args:
        key,value = arg.split('=')
        request_args[key]= value.replace('%2','')
    print(request_args)
    return {
        'statusCode': 200,
        'body': ''
    }
