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
nome_planilha = 'Retiro_0002.xls'

mensagem = ',%0A\
Está%20chegando%20a%20hora%20do%20Retiro%20de%20Meditação.%0A\
Quem%20quer%20serenizar%20a%20mente%20e%20energizar%20o%20corpo%20já%20se%20inscreveu%0A\
Será%20em%20um%20local%20mágico,%20a%2050%20min%20do%20Plano%20Piloto.%20Veja%20um%20álbum%20com%20fotos%20e%20vídeos%20de%20Retiros%20que%20já%20fizemos:%20https://photos.app.goo.gl/C5kM3ca3FPwgJ39S9%0A\
O%20Retiro%20será%20coordenado%20pela%20Profa%20Cristina%20Gobbi,%20estudiosa%20e%20praticante%20de%20Meditação%20desde%201995.%0A\
Quer%20saber%20mais%20sobre%20ela?%20Acesse%20o%20canal%20no%20Youtube%0A\
http://www.youtube.com/c/MeditaçãoHarmoniaeEquilíbrio%0A\
Ou%20conheça%20sua%20Página%20no%20Face%0A\
http://www.facebook.com/meditacaoharmoniaequilibrio/%0A\
Temos%20também%20o%20Perfil%20no%20Insta%0A\
http://www.instagram.com/meditacao_harmonia_equilibrio/%0AE%20o%20Site:%20www.cristinagobbi.com.br%0A\
Temos%20mais%20interessados%20do%20que%20acomodações.%0A\
Só%20falta%20você.%20Vamos?'
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

for counter in range(100):
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

		new_message = name + mensagem

		new_url = new_url + new_message

		print new_url

		browser.get(new_url)

		sleep(10)

		print "clicando"

		browser.find_element_by_class_name("button").click()

		sleep(26)

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