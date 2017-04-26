# -*-coding: utf-8 -*-

import time
from slackclient import SlackClient
import google
import requests
from bot_configs import*        #импортируем настройки из bot_config

def search(what):
    for url in google.search(what, lang='eng',stop=5):
        return (url)

what = {
    'погода': "Погода Отличная, я ж загораю!",
    'жизнь' : "Житуха вапшэ супэр!",
    'менделева': 'нет. не хочу =('
}
you = {
    'дебил': 'Иди в Жопу!',
    'молодец': 'Спасибо, мудак!',
    'lol': 'что смешного???'

}
russian = {
    'норм': 'Я понимаю русский!'
}
Questions = {
    ' what is ': search,


}


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
            print message
            test = 'bender'
            user = slack_message.get("user")
            if message == None or user == None:
                continue
            elif test in message.lower():
                for key,values in Questions.items():
                    if key in message.lower():
                        message_to_user = values(message[6::])
                        sc.rtm_send_message(CHANNEL_NAME, ("<@{}> "+message_to_user).format(user))

       # спим неного
        time.sleep(0.5)
