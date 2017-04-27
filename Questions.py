# -*-coding: utf-8 -*-
import google
import datetime
import random as r

def search(what):
   for url in google.search(what, lang='ru',stop=5):
       return (url)

def what_time(what):
    now = datetime.datetime.now()
    moment = now.time()
    return (str(moment)[:8:])

def hello_answer(hello_answers):
    hello_answers = [line.strip() for line in open("./hello_answers.txt")]
    return "{}".format(r.choice(hello_answers))

def how_are_you(how):
    how = [line.strip() for line in open("./how_are_you.txt")]
    return "{}".format(r.choice(how))

hello_list = ('привет','добрый день','здарова')
how = ('как дела', 'как ты')
time_list = ('который час','сколько время','время')
what_list = ('что такое','кто такой','где найти')

Questions = {
    what_list : search,
    how: how_are_you,
    hello_list: "Приветствую! \n",
    time_list: what_time

}
