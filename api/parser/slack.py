import urllib.parse


class SlackParser():
    data = {}
    def parse(self, event:dict):
        # parse out messages
        self.data = urllib.parse.parse_qs(event['body'])
        # format
        self.data['command'] = self.data['command'][0]
        return self.data