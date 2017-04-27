# -*- coding: utf-8 -*-
#глобальные переменные
BOT_TOKEN =  "token"
CHANNEL_NAME = "channel"
CHAT_BOT_NAME = "бот"   #бывший test='бот'

def search(what):
   for url in google.search(what, lang='ru',stop=5):
       return (url)

def what_time(what):
    now = datetime.datetime.now()
    moment = now.time()
    return (str(moment)[:8:])
