#!/usr/bin/env python
# -*- coding: utf-8 -*-

import facebook
import time

def checarComentado(check):
	counter = 0


	try:
		while counter < len(check['comments']['data']):
			try:
				if check['comments']['data'][counter]['from']['name'] == nameOfPage:
					#print 'respondido'
					return True

				counter = counter + 1

			except KeyError:
				counter = counter + 1
				continue

	except:
		pass
	return False

#teste com a morar_br

quantidade_respondido = 0

id_ev = '1163510226997646'

depilacao_id = 'act_1971824669499527'

#token = 'EAAEfudWPdj0BAE1In9ZAR9A8tZBG4cPg5oWFxfsEpi1tKQ5DieTQ7sEPgUlMYMWyu4T91jwZAGhNS1DhVOR9RzZBoN6t5MzqIqtPnmrHZA8N5J3qvkKpj0zj2uslcP6o5ZBQ13OLQUZCNCLyFNfDHs1V9alZCD61Pps2KWRJW1NwozeOajpBIpHZB'

token = 'EAAEfudWPdj0BAHSt6ZBuvK2FZAGhZBFvmknaKAZC1ohb8tBjzpw6gbLl3eyrVbVYCsjm0lEPg7QC1OvXhpJeJntB1eYDPhZCOoQnXJwAY0pa0LGFFTjpZAnKdNPFT0f8kkbxHuE5u8Y4sNyKusyPHxYVHKxQPNNwTeFa5hsQlNZAgZDZD'

nameOfPage = u'Depilação Laser BR'

graph = facebook.GraphAPI(token, version = '3.2')

ads = graph.get_object(depilacao_id + '?fields=campaigns{adsets{ads}}')

total_campanha = len(ads['campaigns']['data'])

counter_campanha = 0


while counter_campanha < total_campanha:
	total_conjuntoAnuncios = len(ads['campaigns']['data'][counter_campanha]['adsets']['data'])

	counter_conjuntoAnuncios = 0

	while counter_conjuntoAnuncios < total_conjuntoAnuncios:
		total_anuncios = len(ads['campaigns']['data'][counter_campanha]['adsets']['data'][counter_conjuntoAnuncios]['ads']['data'])

		counter_anuncios = 0

		while counter_anuncios < total_anuncios:
			try:
				ad_id =  ads['campaigns']['data'][counter_campanha]['adsets']['data'][counter_conjuntoAnuncios]['ads']['data'][counter_anuncios]['id']

				ad_ef_id = graph.get_object(ad_id + '/?fields=creative.fields(effective_object_story_id),insights.fields(actions)')

				ef_id = ad_ef_id['creative']['effective_object_story_id']

				com = graph.get_object(ef_id + '?fields=comments.limit(1500)')

				print len(com['comments']['data'])

				total_comentario = len(com['comments']['data'])

				counter_comentario = 0

				while counter_comentario < total_comentario:
					comment_id =  com['comments']['data'][counter_comentario]['id']

					comentario = com['comments']['data'][counter_comentario]['message']

					comentario = comentario.upper()

					#print comentario.encode("utf-8")

					counter_comentario = counter_comentario + 1

					if(comentario.find("QUERO") is not -1):
						check = graph.get_object(comment_id + '?fields=comments')

						#print check

						if not checarComentado(check):
							#print check
							#print 'nao respondido'
							quantidade_respondido = quantidade_respondido + 1
							graph.put_comment(comment_id, message = "Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.")


					elif((comentario.find("ONDE") is not -1) or (comentario.find(u"ENDEREÇO") is not -1)):
						check = graph.get_object(comment_id + "?fields=comments")


						if not checarComentado(check):
							quantidade_respondido = quantidade_respondido + 1
							graph.put_comment(comment_id, message = "São mais de 370 unidades em todo Brasil. Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.")
					
				counter_anuncios = counter_anuncios + 1

			except KeyError:
				counter_anuncios = counter_anuncios + 1
				continue
			except Exception as e:
				print e
				#print com
				time.sleep(60)
				pass

		counter_conjuntoAnuncios = counter_conjuntoAnuncios + 1

	counter_campanha = counter_campanha + 1

arq = open('log.txt', 'w')

texto = str(quantidade_respondido) + ' respostas dadas'

arq.write(texto)
arq.close()

#if(comentario.find("QUERO") is not -1):
	#check = graph.get_object(comment_id + '?fields=comments')

	#if not checarComentado(check):
	#graph.put_comment(comment_id, message = "Inscreva-se clicando no link abaixo da imagem, aguarde contato telefônico e aproveite.")