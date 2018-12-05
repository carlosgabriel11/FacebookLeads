import facebook
import requests
import urllib2
#pegar o oken com o acesso a leads
token = 'EAAQhV3JPZCU8BAA7xhnIHb0psJyrMhFy6LgveVxACsKapUS4bIiMNlHptrrN6YqnrBvIzuJS8S4KbfqGK5eGnuZCRx07iIxdnpSUpYF0muLNVC6eRWwIacVtSkTFl31TDovNDptA4o6M83eMHIaklfXBBfmEuS1FfAX4XeOlxU5h1iulcYk1PXdT0DGPwvvPFlK2hQpwZDZD'
graph = facebook.GraphAPI(token)
args = {'fields' : 'leadgen_forms'}
#substituir talvez por get_object(s)
friends = graph.get_object("me", **args)
print friends['leadgen_forms']['data'][0]['leadgen_export_csv_url']

response = urllib2.urlopen(friends['leadgen_forms']['data'][0]['leadgen_export_csv_url'])
html = response.read()

with open('.', 'w') as f:  
    f.write(html) 
