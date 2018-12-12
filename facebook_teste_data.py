import facebook
import os
import calendar
import datetime
import time
from calendar import monthrange
import shutil


#referencia dos dias em que vai pegar os leads
while True:
	dias = input("Voce quer pegar os leads de quantos dias: ")

	if dias <= 0:
		print "Dia invalido"
		continue
	else:
		break

now = datetime.datetime.now()

#pegar o dia de origem que o usuario quer as leads
if dias >= now.day:
	var = dias - now.day
	if now.month == 1:
		ano = now.year
		mes = 12
		dias_do_mes = monthrange(now.year-1, mes)
		dia = dias_do_mes[1] - var
	else:
		ano = now.year
		mes = now.month - 1
	 	dias_do_mes = monthrange(now.year, mes)
	 	dia = dias_do_mes[1] - var
else:
	ano = now.year
	mes = now.month
	dia = now.day - dias

#colocar no formato unix
cal1 = calendar.timegm((ano, mes, dia, 0, 0, 0))
cal2 = calendar.timegm((now.year, now.month, now.day, 0, 0, 0))

#o token com acesso a leads
token = []
#token da Morar_BR
token.append('EAAQhV3JPZCU8BAG0iWwcoKjeQug3wAT9ks4AiAvHGgMyOEj7yIMw67WTnliZB335zizemvBlktZAQRUZCJJZBiLdjI4rm3bgN9c6C985ZAdVPVJEK6ZAgaK93HHFROa7f10ZAXXIZAjPjRC32iHhvmXYX5wyhKay9jU3PmQnclfv4BwZDZD')
#token da Cilios_BR
token.append('EAAQhV3JPZCU8BAOQKUsn7BKZBjxVvrOb40y80pBvE2sOQqQiI3TETjsd01XyZB25ibFRazOhkeXl2IZBQKb6di9n1ZBiXDxHHMpSm3ctfLL4DGoILw4FGrF2FRcA3wZA65HdA5hjy66lHfXkZAOwg2F9BeaMZBOmqEd0DtmMgFJkb3oA2W7TtjGm')

#os argumentos para pegar as leads
args = {'fields' : 'leadgen_forms'}

#o local de download dos arquivos
diret = "C:\\Users\\renderxp\\Downloads\\"

#o contador global
global_counter = 0

while global_counter < len(token):

	graph = facebook.GraphAPI(token[global_counter])

	#pegando o objeto dicionario referente as leads
	friends = graph.get_object("me", **args)

	#baixar os arquivos
	counter = 0

	while counter < len(friends['leadgen_forms']['data']):
		url = friends['leadgen_forms']['data'][counter]['leadgen_export_csv_url']

		url = url[:(url.find("&")+1)] +  "type=form&amp&from_date=" + str(cal1) + "&amp&to_date=" + str(cal2)

		os.system("chrome \"" + url + "\"")

		counter = counter + 1

	time.sleep(2)

	dropdiret = "C:\\Users\\renderxp\\Desktop"
	dropbr = '\\'

	#apagar as leads vazias
	for nome in os.listdir(diret):
		if nome.find(".csv") != -1:
			new_diret = diret + nome

			if os.path.getsize(new_diret) < 350:
				os.remove(new_diret)

	#renomear os arquivos para xls
	for nome in os.listdir(diret):
		if nome.find(".csv") != -1:
			nome = diret + nome
			new_name = nome[:nome.find(".csv")] + ".xls"
			os.rename(nome, new_name)

	#renomear os arquivos para xls
	for nome in os.listdir(diret):
		if nome.find(".xls") != -1:
			nome = diret + nome
			shutil.move(nome,dropdiret)

	for nome in os.listdir(dropdiret):
		if nome.find("Brasil") != -1:
			nome = dropdiret + nome
			shutil.move(nome, dropbr)


	global_counter = global_counter + 1