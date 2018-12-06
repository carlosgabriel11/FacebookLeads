import facebook
import requests
import urllib2
import csv
import os

#pegar o oken com o acesso a leads
token = 'EAAQhV3JPZCU8BANVhG1lml06YP4zrIKdOdArBc8ntGTSd0nRcMtUpg3w42T4ZCDuyI259SxRdn7HZA6aw6no8ohf5WVNoAiFvZA2vZCKnJRA3fiLe9kFaMaZBlVxSsCyoG3rdxqRv5PEAFaXRqRDYLOZByxwgWnHYstlZAnjB1kgW4OaS5rmeQHUhsJ3m1ZCj7JDuHepRZCA8ZB3QZDZD'
graph = facebook.GraphAPI(token)
args = {'fields' : 'leadgen_forms'}
#substituir talvez por get_object(s)
friends = graph.get_object("me", **args)
print "chrome " + friends['leadgen_forms']['data'][0]['leadgen_export_csv_url']

#response = requests.get(friends['leadgen_forms']['data'][0]['leadgen_export_csv_url'])
#html = response.read()

os.system("chrome \"" + friends['leadgen_forms']['data'][0]['leadgen_export_csv_url'] + "\"")
#fp = csv.writer(open("algo.csv", "w"))

#for line in response.content:
#	print line
#	fp.writerow(line)
