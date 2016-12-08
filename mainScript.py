#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import vk_requests
import uuid
import mysql.connector
import requests
import sys
import urllib
import json

groups = {'Евгений Троцкий':'Админ', 'Павел Друов':'Пользователь'}
moneys = {'Евгений Троцкий':'365', 'Павел Дуров':'21'}
users = ['Евгений Троцкий', 'Павел Дуров']

api = vk_requests.create_api(access_token='7adc657fca61dcf8a7794677a83515caef5c3f2a3778d9d2dd99eaec2c5e20f20d278fa38c822464a0a63')
profiles = api.users.get()
username = profiles[0]['first_name']+' '+profiles[0]['last_name']
username.encode('utf-8')

data = {'name' : username}
urllib.parse.urlencode(data)
print(sys.version_info) # запрашиваем версию
response = urllib.request.urlopen("http://kaboom.net/check.php",data)
html = response.read().decode("utf-8") # utf-8 чтобы принять русские буквы
print('Ваше имя: ' + html)

def debug():
	print(locals())
	
#debug()

def auth():
	if(username in users):
		status = api.status.get()
		group = groups.get(username)
		balance = moneys.get(username)
		print('=============AUTH===========')
		print('| Name: ' + username)
		print('| Group: ' + group)
		print('| Balance: ' + balance)
		print('=============AUTH===========')
	else:
		print('Access error')
#auth()
