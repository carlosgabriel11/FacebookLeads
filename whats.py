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
import codecs

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

	new_phone = new_phone + str(phone[0])
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
nome_planilha = 'Mensagem.xlsx'

#name of the file of the message
nome_mensagem = 'Mensagem.txt'

arq = codecs.open(nome_mensagem, encoding='ISO-8859-1')

texto = u''

texto += arq.read()

arq.close()

mensagem = u""

for ch in texto:
	if ch == ' ':
		mensagem += '%20'
	elif ch == '\n':
		mensagem += '%0A'
	else:
		mensagem += ch

#opening the workbook
book = xlrd.open_workbook(nome_planilha)

#opening the first sheet
sh = book.sheet_by_index(0)

#open the google chrome
browser = webdriver.Firefox()

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
	#if counter == 0:
		#continue


	name = sh.cell_value(counter, nome_column)
	print name
	name = name.split(' ')[0]
	name = name.lower()
	name = name.title()

	phone = sh.cell_value(counter, phone_column)

	print phone

	if phone == "":
		continue

	try:
		#phone = treatPhone(phone)

		new_url = url_phone + str(int(phone)) + "&text="
		new_message = name + mensagem
		new_url = new_url + new_message
		print "chegou"

		#print new_url

		browser.get(new_url)

		sleep(10)

		if 'wrong' in browser.page_source:
			counter -= 1
			continue

		if 'Server Error' in browser.page_source:
			counter -= 1
			continue

		print "clicando"

		browser.find_element_by_class_name("button").click()

		sleep(5)

		while True:
			try:
				text_box = browser.find_element_by_class_name("_3u328")
				text_box.send_keys('\n')		

				writeSheet(counter, sh, wsExistente, line_write1)

				line_write1 = line_write1 + 1

				break
			except:
				try:
					if u'inválido' in browser.page_source: #browser.find_element_by_xpath("//div[@class='_2Vo52']").text.find(u'inválido') is not -1:
						print "algo"
						writeSheet(counter, sh, wsInexistente, line_write2)
						line_write2 = line_write2 + 1
						break
				except Exception as e:
					print e
					sleep(5)
					continue

		sleep(10)

	except Exception as e:
		print e
		writeSheet(counter, sh, wsInexistente, line_write2)
		line_write2 = line_write2 + 1
		continue

wbExistente.save('Contato+' + str(datetime.now().year) + '_' + str(datetime.now().month)  + '_' + str(datetime.now().day) + '.xls')
wbInexistente.save('Contato-'+ str(datetime.now().year) + '_' + str(datetime.now().month)  + '_' + str(datetime.now().day) + '.xls')