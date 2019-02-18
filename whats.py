import os

url  = 'https://api.whatsapp.com/send?phone='

number = input('Digite o número de telefone: ')

url = url + number

os.system("chrome \"" + url + "\"")