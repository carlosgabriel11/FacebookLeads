import facebook
import os
import calendar
import datetime
from calendar import monthrange

#referencia dos dias em que vai pegar os leads
dias = input("Voce quer pegar os leads de quantos dias?\n")

#o token com acesso a leads
token = 'EAAEfxROpy9IBAHzfP2SiEd5iEchf7huVrwbDGjbe5d4ORPg9ZBZAWS5OuiDdiYLxnGXmS6uV8J0Xkrh2E0itaFi8hefqQ6RxmZAG0ZC6AUgFtzGAqU5LBJl4wVphzXKnSFHMxWvU8mWA6EN7GQytP0Vak2MaUGrS7M1UMUFmViUZB462diqsPFM9kifXDq3cZD'
graph = facebook.GraphAPI(token)
args = {'fields' : 'leadgen_forms'}
#pegando o objeto dicionario referente as leads
friends = graph.get_object("me", **args)

url = friends['leadgen_forms']['data'][0]['leadgen_export_csv_url']

now = datetime.datetime.now()
if dias >= now.day:
	var = dias - now.day
	if now.month = 1:
		mes = 12
		dias_do_mes = monthrange(now.year-1, mes)
	else:
		mes = now.month - 1
	 	dias_do_mes = monthrange(now.year, mes)
	 dia = dias_do_mes[1] - var
else:
	mes = now.month
	dia = now.day-dias


cal1 = calendar.timegm((now.year, mes, dia, 0, 0, 0))
cal2 = calendar.timegm((now.year, now.month, now.day-1, 24, 0, 0))

url = url[:(url.find("&")+1)] +  "type=form&amp&from_date=" + str(cal1) + "&amp&to_date=" + str(cal2)

print url

os.system("chrome \"" + url + "\"")
#fp = csv.writer(open("algo.csv", "w"))

#for line in response.content:
#	print line
#	fp.writerow(line)