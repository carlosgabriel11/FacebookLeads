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
import clipboard
import sys

reload(sys)

sys.setdefaultencoding('utf8')

phone_column = 1
nome_column = 0
#sexo_column = 18
line_write1 = 0
line_write2 = 0

def treatPhone(phone):
	new_phone = ""

	if phone == "":
		return phone

	new_phone = new_phone + str(phone[1])
	new_phone = new_phone + str(phone[2])
	new_phone = new_phone + str(phone[3])
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
nome_planilha = 'Lista_Retiro001.xls'

with open('texto.txt', 'r') as f:
	conteudo = f.read()
	clipboard.copy(',%0A\
Estou%20enviando%20informações%20sobre%20o%20Retiro%20de%20Meditação%20de%2013%20e%2014%20de%20%20abril.%0A\
Será%20no%20Paraíso%20na%20Terra,%20um%20local%20de%20natureza%20preservada,%20com%20muito%20ar%20puro,%20cachoeiras,%20canto%20de%20pássaros%20e%20quietude%20a%2040%20minutos%20do%20Plano%20Piloto%20(Brasília).%0A\
No%20Retiro%20temos%20resultados%20incríveis%20de%20relaxamento,%20alegria%20e%20união%20de%20pessoas%20com%20o%20mesmo%20propósito:%20ter%20Harmonia%20e%20Equilíbrio%20em%20suas%20vidas.%0A\
Serão%202%20dias%20dedicados%20a%20variadas%20práticas%20meditativas,%20com%20%20exercícios%20de%20silenciamento,%20serenização,%20contemplações,%20caminhadas%20e,%20para%20os%20que%20apreciam,%20banhos%20de%20cachoeira.%20Tudo%20isto,%20em%20meio%20ao%20verde%20da%20natureza,%20com%20uma%20alimentação%20super%20leve%20e%20natural.%0A\
%0A\
Informações%0A\
Data:%20Sábado%20e%20Domingo,%20dias%2013%20e%2014/04/2019%0A\
Período:%20de%207:30h%20de%20sábado%20(13/04)%20às%2016:00h%20de%20domingo%20(14/04).%0A\
Local:%20Reserva%20Ecológica%20Paraíso%20na%20Terra%20em%20Brazlândia%20–%20DF,%20que%20fica%20a%2050%20min%20do%20Plano.%0A\
Incluído%20no%20programa:%20Ensinamentos%20e%20vivências%20de%20Meditação%20Mindfulness.%20Hospedagem%20e%20alimentação%20completa%20(café%20da%20manhã,%20almoço,%20jantar%20e%20coffee-break%20no%20sábado%20e%20café%20da%20manhã,%20coffee-break%20e%20almoço%20no%20domingo).%0A\
Valores%0A\
Qto%20triplo:%20R$%20570%20à%20vista%20ou%20em%202%20x%20de%20R$%20315%0A\
Qto%20duplo:%20R$%20590%20à%20vista%20ou%20em%202%20x%20de%20R$%20330%0A\
Qto%20casal%20(por%20pessoa):%20R$%20590%20à%20vista%20ou%20em%202%20x%20de%20R$%20330%0A\
Qto%20individual:%20R$%20690%20à%20vista%20ou%20em%202%20x%20de%20R$%20390%0A\
%0A\
Se%20você%20desejar%20viver%20essa%20experiência,%20é%20só%20responder%20essa%20mensagem%20que%20entraremos%20em%20contato%20por%20telefone.%0A\
%0A\
André')

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

	try:
		phone = treatPhone(phone)

		new_url = url_phone + phone + "&text="

		new_message = name + clipboard.paste()

		new_url = new_url + new_message

		browser.get(new_url)

		sleep(10)

		print "clicando"

		browser.find_element_by_class_name("button").click()

		sleep(10)

		text_box = browser.find_element_by_class_name("_2S1VP")
		text_box.send_keys('\n')		

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