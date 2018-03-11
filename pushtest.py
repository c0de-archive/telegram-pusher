import os
import pusher
import logging
import uuid
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

pusher_client = pusher.Pusher(
  app_id=os.environ['pusher_appid'],
  key=os.environ['pusher_key'],
  secret=os.environ['pusher_secret'],
  cluster='us2',
  ssl=True
)

updater = Updater(token=os.environ['telegram_token'])
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

ids = dict({})

def _save_id(id, chat_id):
  ids[chat_id] = {
    'id': id,
    'chat_id': chat_id
  }
  return str(ids[chat_id]['id'])

def generate_id(chat_id):
  return _save_id(uuid.uuid4(), chat_id)

def start(bot, update):
  chat_id = update.message.chat_id
  bot_msg = "Visit https://dev.c0defox.es/push/?channel=%s\
             and then come back to say something to me!" % generate_id(chat_id)
  bot.send_message(chat_id=chat_id, text=bot_msg)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
  chat_id = update.message.chat_id
  # Send the push notification to the session (uuid)
  pusher_client.trigger(str(ids[chat_id]['id']), 'my-event',
                        {'message': update.message.text})
  bot.send_message(chat_id=chat_id, text="Notification Sent!")

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
# pusher_client.trigger('my-channel', 'my-event', {'message': 'I\'m a fox! :3'})

# Start being a TG bot
updater.start_polling()

