#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import xlwt
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

def treatPhone(phone):
	new_phone = ""

	if phone[0] == '(':
		new_phone = new_phone + phone[1]
		new_phone = new_phone + phone[2]
		new_phone = new_phone + phone[5]
		new_phone = new_phone + phone[6]
		new_phone = new_phone + phone[7]
		new_phone = new_phone + phone[8]
		new_phone = new_phone + phone[10]
		new_phone = new_phone + phone[11]
		new_phone = new_phone + phone[12]
		new_phone = new_phone + phone[13]
		new_phone = new_phone + phone[14]

		return new_phone

	else:
		return phone

#the url of the whatsapp
url = 'https://web.whatsapp.com'

#the url of the whatsapp with the phone
url_phone  = 'https://api.whatsapp.com/send?phone='

#the name of the workbook
nome_planilha = 'Leads.xlsx'

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

wb = xlwt.Workbook()

ws = wb.add_sheet("Funcionou")

for counter in range(sh.nrows):
	if counter == 0:
		continue

	name = sh.cell_value(counter, 1)
	name = name.split(' ')[0]
	name = name.lower()
	name = name.title()

	phone = sh.cell_value(counter, 17)

	try:
		phone = treatPhone(phone)

		new_url = url_phone + "55" + str(int(phone))

		browser.get(new_url)

		sleep(10)

		browser.find_element_by_class_name("button").click()

		sleep(10)

		ws.write(counter, 0, name)
		ws.write(counter, 1, phone)

	#new_message = u'Olá ' + name + '. ' + message + "\n"
	#text_box = browser.find_element_by_class_name("_2S1VP")
	#text_box.send_keys(new_message)

	#sleep(10)

	except Exception as e:
		print e
		continue

wb.save('teste.xls')