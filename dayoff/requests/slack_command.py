# https://api.slack.com/slash-commands
#
# token=gIkuvaNzQIHg97ATvDxqgjtO
# team_id=T0001
# team_domain=example
# channel_id=C2147483705
# channel_name=test
# user_id=U2147483697
# user_name=Steve
# command=/weather
# text=94070
# response_url=https://hooks.slack.com/commands/1234/5678

from wtforms import Form, StringField, validators

# curl localhost:5000/dayoff \
# -d 'token=my_token' \
# -d 'team_id=my_team_id' \
# -d 'team_domain=my_team_domain' \
# -d 'channel_id=my_channel_id' \
# -d 'channel_name=my_channel_name' \
# -d 'user_id=my_user_id' \
# -d 'user_name=my_user_name' \
# -d 'command=my_command' \
# -d 'text=my_text' \
# -d 'response_url=my_response_url'

class SlackCommandRequest(Form):
    token = StringField('access_token', [validators.DataRequired()])
    team_id = StringField('team_id', [validators.DataRequired()])
    team_domain = StringField('team_domain', [validators.DataRequired()])
    channel_id = StringField('channel_id', [validators.DataRequired()])
    channel_name = StringField('channel_name', [validators.DataRequired()])
    user_id = StringField('user_id', [validators.DataRequired()])
    user_name = StringField('user_name', [validators.DataRequired()])
    command = StringField('command', [validators.DataRequired()])
    text = StringField('text', [validators.DataRequired()])
    response_url = StringField('response_url', [validators.DataRequired()])
