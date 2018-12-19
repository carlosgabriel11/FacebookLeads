Passo 1 - instalar o python 2.7:
1.1 - Abrir o link https://www.python.org/downloads/windows
1.2 - Procurar o python 2.7.9
1.3 - Clicar em Download Windows x86-64 MSI installer
1.4 - Executar o arquivo baixado python-2.7.9.amd64.msi
Obs: Provavelmente ele será instalado no local C:\Python27\

Passo 2 - Colocar o python na Path:
2.1 - Procurar o local de instalação do python dentro do C:
2.2 - Dentro do local de instalação do python, no local onde fica a localização do diretório, clica-se com o botão direito do mouseem python 27 e clica em "Copiar endereço como texto"
2.3 - No explorador de arquivos, do lado esquerdo, procurar pelo computador (my computer)
2.4 - Clicar sobre o ícone do computador com o botão direito do mouse e procurar por propriedades
2.7 - Na nova janela que abrir, clicar em "configurações avançadas do sistema"
2.8 - Após isso, clicar em variáveis de ambiente
2.9 - Clicar em Path e em seguida em editar
2.10 - Adicionar o endereço copiado

Passo 3 - Dar upgrade no "pip"
3.1 - Com Windows + R, vai aparecer o recurso de executar do Windows. Digite "cmd" para abrir o prompt.
3.2 - Digitar o comando "cd \Python27\Scripts" para mudar de diretório.
3.3 - Digitar o comando "pip install --upgrade pip"

Passo 4 - Baixar as libs dependentes
4.1 - Ainda no mesmo prompt que foi usado no passo anterior, digite "pip install facebook-sdk" para instalar a biblioteca do facebook
4.2 - Em seguida, quando acabar a instalação do passo anterior, digite "pip install pywin32" para instalar a biblioteca de manipulação de planilhas do excel 