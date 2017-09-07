------------
slack-dayoff
------------

# umm, what?

a rudimentary app to take days off on Slack...


no, in fact, it is more an exercise to do some Python!

# slack commands

- `/dayoff help`: to display available commands
- `/dayoff YYYY-mm-dd`: to take a day off (eg: `/dayoff 2025-01-02`)
- `/dayoff ls`: list the three upcoming days off

# run the app

```
git clone https://github.com/pzn/slack-dayoff.git
cd slack-dayoff
pip install -r requirements.txt
python3 manage.py db upgrade
python3 manage.py runserver
```

and read `config.py` for the required variables to run the app.

# live demo

the app is deployed on Heroku, and there is a Slack app available!

there is no UI on this app (yet?), so you will have to click on the following
URL by yourself: https://slack.com/oauth/authorize?&client_id=126549707972.236976598518&scope=commands,chat:write:bot

enjoy some slack!
