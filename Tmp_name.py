# -*-coding: utf-8 -*-
import time
from slackclient import SlackClient

BOT_TOKEN = "token"
CHANNEL_NAME = "channel"

def main():
    sc = SlackClient(BOT_TOKEN)

    # присоеденяемся к слаку
    if sc.rtm_connect():
        # шлем приветсвие
        sc.rtm_send_message(CHANNEL_NAME, "Я снова жив!!!")

        while True:
            # читаем сообщения 
            for slack_message in sc.rtm_read():
                message = slack_message.get("text")
                user = slack_message.get("user")
                if not message or not user:
                    continue
                sc.rtm_send_message(CHANNEL_NAME, "<@{}> отвали от меня , я ничего не умею еще".format(user))
            # спим неного
            time.sleep(0.5)
    else:
        print("Что-то пошло не так . не могу подключится")

if __name__ == '__main__':
    main()
