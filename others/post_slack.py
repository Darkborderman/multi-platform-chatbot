import json
import requests
from config import SLACK_WEBHOOK

requests.post(
    SLACK_WEBHOOK,
    headers={
        'Content-Type':'Application/json'
    },
    data=json.dumps({})
)