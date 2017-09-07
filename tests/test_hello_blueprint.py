from flask import Flask
from unittest import mock, TestCase


app = Flask(__name__)
from dayoff.controllers import HelloBlueprint
app.register_blueprint(HelloBlueprint, url_prefix='')


class HelloBlueprintTestCase(TestCase):

    def setUp(self):
        self.app = app.test_client()

    @mock.patch('dayoff.controllers.hello.OauthAccessRequestHandler')
    def test_can_handle_valid_request(self, mock):

        # given
        query_string = self._sane_query_string('my_code', 'my_state')

        # execute
        res = self.app.get('/hello', query_string=query_string)

        # verify
        self.assertEqual(res.status_code, 202)

    @mock.patch('dayoff.controllers.hello.OauthAccessRequestHandler')
    def test_when_code_is_missing__should_return_http_400(self, mock):

        # given
        query_string = self._sane_query_string(None, 'my_state')

        # execute
        res = self.app.get('/hello', query_string=query_string)

        # verify
        self.assertEqual(res.status_code, 400)

    @mock.patch('dayoff.controllers.hello.OauthAccessRequestHandler')
    def test_when_state_is_missing__should_be_good(self, mock):

        # given
        query_string = self._sane_query_string('my_code', None)

        # execute
        res = self.app.get('/hello', query_string=query_string)

        # verify
        self.assertEqual(res.status_code, 202)

    def _sane_query_string(self, code=None, state=None):
        d = {'code': code, 'state': state}
        return {k: v for k, v in d.items() if v is not None}
