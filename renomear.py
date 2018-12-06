import os

diret = 'C:\\Users\\renderxp\\Downloads'

for nome in os.listdir("."):
	if nome.find(".csv") != -1:
		new_name = nome[:nome.find(".csv")] + ".xls"
		os.rename(nome, new_name)