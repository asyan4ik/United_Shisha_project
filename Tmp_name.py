# -*-coding: utf-8 -*-
import time
from slackclient import SlackClient
from bot_config import*
from Questions import Questions

if __name__ == '__main__':
   sc = SlackClient(BOT_TOKEN)

 # присоеденяемся к слаку
   if sc.rtm_connect():
       # шлем приветсвие
       sc.rtm_send_message(CHANNEL_NAME, "Ready for Work!")
   while True:
       # читаем сообщения
       for slack_message in sc.rtm_read():
           message = slack_message.get("text")
           user = slack_message.get("user")
           if message == None or user == None:
               continue
           elif CHAT_BOT_NAME in message.lower().encode('utf-8'):
               for key,values in Questions.items():
                   for vars in key:
                       if vars in message.lower().encode('utf-8'):
                           print(type(values))
                           if type(values) == str:
                               message_to_user = values
                               sc.rtm_send_message(CHANNEL_NAME, ("<@{}> " + message_to_user).format(user))
                           else:
                               message_to_user = values(message[6::].encode('utf-8'))
                               sc.rtm_send_message(CHANNEL_NAME, ("<@{}> "+message_to_user).format(user))
       time.sleep(1)
