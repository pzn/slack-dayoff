from flask import Flask
from unittest import mock, TestCase


app = Flask(__name__)
from dayoff.controllers import DayOffBlueprint
app.register_blueprint(DayOffBlueprint, url_prefix='')


class DayOffBlueprintTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()

    @mock.patch('dayoff.controllers.dayoff.LsRequestHandler')
    def test_can_handle_valid_request(self, mock):

        # given
        data = self._given_slack_command_dict('ls')

        # execute
        res = self.app.post('/dayoff', data=data)

        # verify
        self.assertEqual(res.status_code, 202)

    @mock.patch('dayoff.controllers.dayoff.LsRequestHandler')
    def test_when_field_is_missing__should_return_http_400(self, mock):
        for key in self._given_slack_command_dict('ls'):
            # given
            data_with_missing_field = self._given_slack_command_dict('ls')
            del data_with_missing_field[key]

            # execute
            res = self.app.post('/dayoff', data=data_with_missing_field)

            # verify
            self.assertEqual(res.status_code, 400, f'field "{key}" is missing from request, and ' \
                                                    'server response is expected to be 400')

    def _given_slack_command_dict(self, text):
        return {'token': 'my_token',
                'team_id': 'my_team_id',
                'team_domain': 'my_team_domain',
                'channel_id': 'my_channel_id',
                'channel_name': 'my_channel_name',
                'user_id': 'my_user_id',
                'user_name': 'my_user_name',
                'command': 'my_command',
                'text': text,
                'response_url': 'my_response_url'}