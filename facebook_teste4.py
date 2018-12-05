import facebook
#pegar o oken com o acesso a leads
token = 'EAAQhV3JPZCU8BAGY4fynpKolnXsU7IhF3asMEZAZA2dIl01QepzjSpjlIftpi60FbtuoYIeNfTYSb5ITEnOEH60nf51mOPyftuZAqcu6H4hZA1cYy1JK3AZCR56ZCMP9rHkj33j5zj8JbrfkgSZABrsWWjjq32UejwNLiExihKUWDb0MHk2ErfCdb742XFKQbew2P8uALJJyuAZDZD'
graph = facebook.GraphAPI(token)
#no facebook business, pegar todos os fields que existem com o metadata=1 e substituir o nome pelo id do usuário business
args = {'fields' : 'colocar o field da lead'}
#substituir talvez por get_object(s)
friends = graph.get_connections("275176122991882", "")
print friends