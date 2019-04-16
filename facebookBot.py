#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import xlrd
import openpyxl
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from datetime import datetime

erro_dropdown = 0

#a function to check if the comment was answered
def checkAnswer(contador, listOfNames):
	if len(listOfNames) == 1:
		return False

	if listOfNames[contador + 1] == u"DEPILAÇÃO LASER BR":
		return True
	else:
		return False


#get the name and the message
def getNameAndMessage(browser):
	counter = 0

	auxText = []
	auxName = []
	auxiliarName = ""
	auxiliarText = ""

	while counter < len(browser.find_elements_by_xpath("//div[@class='_3b-9 _j6a']/div/div")):
		try:
			#the case the person tagged someone else
			auxiliarText =  browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(counter+1) + "]/div/div/div/div[2]/div/div/div/div/div/div/span/div/span[2]/span/span/span/a").text.upper()
			auxiliarName =  browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(counter+1) + "]/div/div/div/div[2]/div/div/div/div/div/div/span/div/span[1]/a").text.upper()
		except Exception as e:
			try:
				#the case the person didn't tagged someone else
				auxiliarText = browser.find_elements_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(counter+1) + "]/div/div/div/div[2]/div/div/div/div/div/div/span/div/span[2]/span/span/span/span")[0].text.upper()
				auxiliarName = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(counter+1) + "]/div/div/div/div[2]/div/div/div/div/div/div/span/div/span[1]/a").text.upper()
				pass
			except:
				try:
					#the case that is an answer
					auxiliarText =  browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(counter+1) + "]/div/div/div/div/div[2]/div/div/div/div/div/div/span/div/span[2]/span/span/span/span").text.upper()
					auxiliarName =  browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(counter+1) + "]/div/div/div/div/div[2]/div/div/div/div/div/div/span/div/span[1]/a").text.upper()
				except:
					pass
			pass
		pass

		try:
			print auxiliarText
			print auxiliarName

		except:
			pass

		auxText.append(auxiliarText)
		auxName.append(auxiliarName)

		auxiliarText = ""
		auxiliarName = ""

		counter = counter + 1

	return auxName, auxText

#answer the messages in the screen
def answer(browser, auxName, auxText):
	auxCounter = 0

	respostas = 0

	global_counter = len(auxText)

	while auxCounter < global_counter:
		try:
			if auxText[auxCounter].find("QUERO") is not -1:
				print "chegou"

				if (not checkAnswer(auxCounter, auxName)) and (auxName[auxCounter] is not u"DEPILAÇÃO LASER BR"):
					print "nao respondido"
					print auxName[auxCounter]

					#click to answer
					elem = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(auxCounter + 1 + respostas) + "]/div/div/div/div[2]/div/div/div/div[2]/a[1]")
					browser.execute_script("arguments[0].click();", elem)
					sleep(4)
					elem = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(auxCounter + 2 + respostas) + "]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div")
					#elem = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(auxCounter + 2 + respostas) + "]/div/div/div[2]/div/div/div/div[1]/input")
					#elem.click()
					#print "clicou"
					#sleep(3)
					#browser.execute_script("arguments[0].innerText = '" + u"Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.\\n" + "';", elem)
					#sleep(10)
					#elem.submit()
					elem.send_keys(u"Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.\n")

					sleep(10)
					respostas = respostas + 1

			if (auxText[auxCounter].find("ONDE") is not -1) or (auxText[auxCounter].find(u"ENDEREÇO") is not -1):
				print "chegou"

				if not checkAnswer(auxCounter, auxName):
					print "nao respondido"
					print auxName[auxCounter]

					#click to answer
					elem = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(auxCounter + 1 + respostas) + "]/div/div/div/div[2]/div/div/div/div[2]/a[1]")
					browser.execute_script("arguments[0].click();", elem)
					sleep(4)
					elem = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(auxCounter + 2 + respostas) + "]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div")
					#elem = browser.find_element_by_xpath("//div[@class='_3b-9 _j6a']/div/div[" + str(auxCounter + 2 + respostas) + "]/div/div/div[2]/div/div/div/div[1]/input")
					#elem.click()
					#print "clicou"
					#sleep(3)
					#browser.execute_script("arguments[0].innerText = '" + u"Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.\\n" + "';", elem)
					#sleep(10)
					#elem.submit()
					elem.send_keys(u"São mais de 370 unidades em todo Brasil. Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.\n")

					sleep(10)
					respostas = respostas + 1

		except Exception as e:
			print e
			pass

		auxCounter = auxCounter + 1

	return respostas

def initFunction(url, url_inbox):
	#open the google chrome
	browser = webdriver.Firefox()

	#open the whatsapp web
	browser.get(url)

	browser.maximize_window()

	#wait for the login of the user
	wait = raw_input("Aperte qualquer tecla assim que logar no facebook: ")

	#give some time to update the page
	sleep(10)

	#try to go directly to the inbox
	browser.get(url_inbox)

	#give some time to update the page
	sleep(10)

	#click in the instagram part
	browser.find_elements_by_class_name("_6ie2")[1].click()

	sleep(10)

	return browser

def selectTheCampaigns(browser):
	global_counter = len(browser.find_elements_by_xpath("//div[@class='_24tx']/div")) - 2

	total_answered = 0

	preto = True

	for counter in range(global_counter):
		erros = 0
		while True:		
			try:
				try:
					if counter == 0:
						auxiliar = browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _2tms _5m15']")
						preto = False
					else:
						auxiliar = browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _5m15']")
						preto = False

				except:
					if counter == 0:
						print browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _2tms _284c _5m15']")
					else:
						print browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _284c _5m15']")					
				browser.find_elements_by_xpath("//div[@class='_24tx']/div")[counter].click()
				break
			except Exception as e:
				sleep(1)
				erros = erros + 1
				if erros == 3:
					erros = 0
					counter = counter + 1

				print e
				continue


		sleep(10)

		nome, mensagem = getNameAndMessage(browser)
		answered = answer(browser, nome, mensagem)

		if answered == 0:
			print "escuro"
			if preto:
				browser.find_element_by_xpath("//div[@class='_3bwx']/div/div").click()

		total_answered = total_answered + answered

		preto = True

	return total_answered

def dropDown(browser,erro_dropdown):
	print "arrastar"

	if erro_dropdown == 3:
		source_elem = browser.find_element_by_xpath("//div[@class='_1t0r _1t0s _4jdr _1t0v']/div")
		erro_dropdown = 0
	else:
		source_elem = browser.find_element_by_xpath("//div[@class='_1t0r _1t0s _4jdr']/div")				

	source_elem.click()

	sleep(5)

	dest_elem = browser.find_elements_by_xpath("//div[@class='_24tx']/div")[9]

	sleep(5)

	ActionChains(browser).drag_and_drop(source_elem, dest_elem).perform()

def checkToAnswer(browser):
	global_counter = len(browser.find_elements_by_xpath("//div[@class='_24tx']/div")) - 2

	for counter in range(global_counter):
		erros = 0
		while True:		
			try:
				try:
					if counter == 0:
						auxiliar = browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _2tms _5m15']")
					else:
						auxiliar = browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _5m15']")

				except:
					if counter == 0:
						auxiliar = browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _2tms _284c _5m15']")
						return True
					else:
						auxiliar = browser.find_element_by_xpath("//div[@class='_24tx']/div[" + str(counter + 1) + "]/div[@class='_4k8w _75uw _5_n1 _284c _5m15']")	
						return True				
				break
			except Exception as e:
				sleep(1)
				erros = erros + 1
				if erros == 3:
					erros = 0
					counter = counter + 1

				print e
				continue

	return False

def main(erro_dropdown):
	#the total number of answers given
	respostas_total = 0

	#the url of facebook
	url = 'https://www.facebook.com/'

	#the url of the inbox
	url_inbox = 'https://business.facebook.com/depilacao.laser.br/inbox/?business_id=1163510226997646&mailbox_id=275176122991882&selected_item_id=100001503612000'

	#the number of dropdowns
	N = 1

	counter = 0

	browser = initFunction(url, url_inbox)
	while (counter < N) or checkToAnswer(browser):		
		respostas_total = respostas_total + selectTheCampaigns(browser)
		while True:
			try:
				dropDown(browser,erro_dropdown)
				erro_dropdown = 0
				break
			except Exception as e:
				print e
				erro_dropdown = erro_dropdown + 1
				sleep(5)
				continue
		sleep(3)

		counter = counter + 1

	print respostas_total

main(erro_dropdown)