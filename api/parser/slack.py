import urllib.parse


class SlackParser():

    def parse(self, event:dict):
        # parse out messages
        return urllib.parse.parse_qs(event['body'])
