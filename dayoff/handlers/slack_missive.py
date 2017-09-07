from .t import T
from dayoff import app
from dayoff.exceptions import SlackMissiveException
import json, requests


class SlackMissive(T):

    def __init__(self, access_token, channel, text):
        self.post_message_url = app.config.get('SLACK_POST_MESSAGE_URL')
        self.access_token = access_token
        self.channel = channel
        super().__init__(text)

    def handle(self, text):
        r = requests.post(url=self.post_message_url,
                          params=self._build_post_message_request(text))

        if r.status_code != 200:
            raise SlackMissiveException('Could not send message to Slack', r.content)

        json = r.json()
        if json['ok'] == False:
            print(json)
            raise SlackMissiveException('Could not send message to Slack', r.content)

    def _build_post_message_request(self, text):
        return {
            'token': self.access_token.access_token,
            'channel': self.channel,
            'text': text
        }
