def slack_formatter(data:dict):
    
    return {
        "text": f"*{data['title']}*\n {data['description']}\n {data['URL']}",
        "mrkdwn": True
    }
