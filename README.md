# telegram-pusher

This is some dumb thing that will take messages from telegram
and relay through https://pusher.com to a web application.

I've provided a simple PHP script that does a channel thing to
show a "notification". On my Nexus 6P, if the phone is unlocked,
and the page is still loaded while Chrome is in memory, the alert
will bring the user to my notification page

## Getting Started

* Clone this repo and enter it
* $ `virtualenv venv`
* $ `source venv/bin/activate`
* $ `pip install -r requirements.txt`
* Register with the Telegram Botfather (https://telegram.me/botfather) 
* Register with Pusher (https://pusher.com)
* create set_env.sh with the following environment variables and fill them with the corrosponding values
  * telegram_token
  * pusher_appid
  * pusher_key
  * pusher_secret
* $ `python pushtest.py`
* On your web server, place the index.php file and allow it to get arguments
* edit the index.php to have your pusher appid
* send your bot `/start` to see if it responds

## Demo

* Visit http://t.me/c0dePushNotifyBot and do /start
* You will be given a link to https://dev.c0defox.es/push/?channel=<channel-id-here>
* Send this link to people you want to recieve the notification
* Post a message to the telegram bot

IDK what will happen if you try to send a message to the bot without doing a /start first
