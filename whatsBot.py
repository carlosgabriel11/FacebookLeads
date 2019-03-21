#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import xlwt
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from datetime import datetime
import urllib

phone_column = 24
nome_column = 3
sexo_column = 18
line_write1 = 0
line_write2 = 0

def treatPhone(phone):
	new_phone = ""

	if phone == "":
		return phone

	new_phone = new_phone + str(phone[1])
	new_phone = new_phone + str(phone[2])
	new_phone = new_phone + str(phone[4])
	new_phone = new_phone + str(phone[5])
	new_phone = new_phone + str(phone[6])
	new_phone = new_phone + str(phone[7])
	new_phone = new_phone + str(phone[8])
	new_phone = new_phone + str(phone[9])
	new_phone = new_phone + str(phone[10])
	new_phone = new_phone + str(phone[11])
	new_phone = new_phone + str(phone[12])
	new_phone = new_phone + str(phone[13])
	new_phone = new_phone + str(phone[14])


	print new_phone

	return new_phone

def writeSheet(line, sh, ws, line_write):
	for counter in range(sh.ncols):
		ws.write(line_write, counter, sh.cell_value(line, counter))


#the url of the whatsapp
url = 'https://web.whatsapp.com'

#the url of the whatsapp with the phone
url_phone  = 'https://api.whatsapp.com/send?phone='

#the name of the workbook
nome_planilha = 'Leads.xlsx'

#mensagem para enviar se a pessoa for do sexo feminino
messageFem = u'Tentei contactá-la via telefone mas sem sucesso. Escrevo em nome do Instituto Assistencial dos Servidores do Distrito Federal (IGDF) e meu nome é Marlon. Trabalhamos com um Plano de Saúde exclusivo para Servidores do GDF. Se você já tem um plano de saúde mas está insatisfeita ou não tem plano mas sonha em ter, me avise o melhor momento durante esta semana para que eu possa entrar em contato? Obrigado!'

#mensagem para enviar se a pessoa for do sexo masculino
messageMas = u'Tentei contactá-lo via telefone mas sem sucesso. Escrevo em nome do Instituto Assistencial dos Servidores do Distrito Federal (IGDF) e meu nome é Marlon. Trabalhamos com um Plano de Saúde exclusivo para Servidores do GDF. Se você já tem um plano de saúde mas está insatisfeito ou não tem plano mas sonha em ter, me avise o melhor momento durante esta semana para que eu possa entrar em contato? Obrigado!'

#opening the workbook
book = xlrd.open_workbook(nome_planilha)

#opening the first sheet
sh = book.sheet_by_index(0)

#open the google chrome
browser = webdriver.Chrome()

#open the whatsapp web
browser.get(url)

#wait for the person register itself in the whatsapp web
wait = raw_input('Digite algo assim que se conectar no whatsapp web: ')

#wait 5 seconds after this.

sleep(5)

wbExistente = xlwt.Workbook()

wsExistente = wbExistente.add_sheet("Existente")

wbInexistente = xlwt.Workbook()

wsInexistente = wbInexistente.add_sheet("Inexistente")

for counter in range(sh.nrows):
	if counter == 0:
		continue

	print "chegou"

	name = sh.cell_value(counter, nome_column)
	name = name.split(' ')[0]
	name = name.lower()
	name = name.title()

	phone = sh.cell_value(counter, phone_column)

	if phone == "":
		continue

	sexo = sh.cell_value(counter, sexo_column)

	try:
		phone = treatPhone(phone)

		new_url = url_phone + phone

		browser.get(new_url)

		sleep(10)

		print "clicando"

		browser.find_element_by_class_name("button").click()

		sleep(10)

		if sexo == 'MAS':
			print "masculino"
			new_message = u'Olá ' + name + '. ' + messageMas + "\n"
			text_box = browser.find_element_by_class_name("_2S1VP")
			text_box.send_keys(new_message)

		if sexo == 'FEM':
			print "feminino"
			new_message = u'Olá ' + name + '. ' + messageFem + "\n"
			text_box = browser.find_element_by_class_name("_2S1VP")
			text_box.send_keys(new_message)

		writeSheet(counter, sh, wsExistente, line_write1)

		line_write1 = line_write1 + 1

		sleep(10)

	except Exception as e:
		print e
		writeSheet(counter, sh, wsInexistente, line_write2)
		line_write2 = line_write2 + 1
		continue

wbExistente.save('Contato+' + str(datetime.now().year) + '_' + str(datetime.now().month)  + '_' + str(datetime.now().day) + '.xls')
wbInexistente.save('Contato-'+ str(datetime.now().year) + '_' + str(datetime.now().month)  + '_' + str(datetime.now().day) + '.xls')