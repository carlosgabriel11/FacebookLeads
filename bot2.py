#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

#the url of the whatsapp
url = 'https://web.whatsapp.com'

#the url of the whatsapp with the phone
url_phone  = 'https://api.whatsapp.com/send?phone='

#the name of the workbook
nome_planilha = 'teste2.xlsx'

#the message to send 
message = u'Tentamos contactá-la durante esta semana mas caiu na caixa postal. Escrevo em nome do Instituto Assistencial dos Servidores do Distrito Federal (IGDF) e meu nome é Raissa. Trabalhamos com um Plano de Saúde, de baixo custo, exclusivo para Servidores do GDF. Se você já tem um plano de saúde mas está insatisfeita ou não tem plano mas sonha em ter, me avise o melhor momento durante esta semana para que eu possa entrar em contato? Obrigada!'

#opening the workbook
book = xlrd.open_workbook(nome_planilha)

#opening the first sheet
sh = book.sheet_by_index(0)

#open the google chrome
browser = webdriver.Chrome()

#open the whatsapp web
browser.get(url)

#wait for the person register itself in the whatsapp web
wait = raw_input()

#wait 5 seconds after this
sleep(5)

for counter in range(sh.nrows):
	if counter == 0:
		continue

	name = sh.cell_value(counter, 0)
	name = name.split(' ')[0]
	name = name.lower()
	name = name.title()

	phone = sh.cell_value(counter, 1)

	new_url = url_phone + "55" + str(int(phone))

	browser.get(new_url)

	sleep(10)

	browser.find_element_by_class_name("button").click()

	sleep(10)

	new_message = u'Olá ' + name + '. ' + message + "\n"
	text_box = browser.find_element_by_class_name("_2S1VP")
	text_box.send_keys(new_message)

	sleep(10)