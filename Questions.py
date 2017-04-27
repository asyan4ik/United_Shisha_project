# -*-coding: utf-8 -*-
from bot_config import search, what_time
hello_list = ('привет','добрый день','здарова')
time_list = ('который час','сколько время','время')
what_list = ('что такое','кто такой','где найти')

Questions = {
    what_list : search,
    hello_list: "Приветствую! \n",
    time_list: what_time

}
