import facebook
import os
import calendar

#o token com acesso a leads
token = 'EAAQhV3JPZCU8BANqyrGkNLWYcphgmccs1xzfMipAODSZAitVRjZAfEiVbtexyyZCqkvMq9t3QcpJZBQdA9ChkHcO0zGnM2ZCZC3vqP0tAylNdevdwgIuF0IrFZCZCRLz7lcjhPx1PbQtOW7pYAHFPeeiQ8eO87iCVp8jZCzqhBbTO64jlbpKSJpoiDZCUXdTAedhEnzGogwKlq9MAZDZD'
graph = facebook.GraphAPI(token)
args = {'fields' : 'leadgen_forms'}
#pegando o objeto dicionario referente as leads
friends = graph.get_object("me", **args)

url = friends['leadgen_forms']['data'][0]['leadgen_export_csv_url']

cal1 = calendar.timegm((2018, 11, 8, 24, 0, 0))
cal2 = calendar.timegm((2018, 11, 11, 24, 0, 0))

url = url[:(url.find("&")+1)] +  "type=form&amp&from_date=" + str(cal1) + "&amp&to_date=" + str(cal2)

print url

os.system("chrome \"" + url + "\"")
#fp = csv.writer(open("algo.csv", "w"))

#for line in response.content:
#	print line
#	fp.writerow(line)
