import json
import urllib.parse


class SlackParser():
    data = {}
    def parse(self, event: dict):
        # parse out messages
        self.data = urllib.parse.parse_qs(event['body'])
        print(self.data)
        # format
        if 'command' in self.data:
            self.data['command'] = self.data['command'][0]

        if 'payload' in self.data:
            self.data = json.loads(self.data['payload'][0])

        return self.data
