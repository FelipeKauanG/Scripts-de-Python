#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib.request

import urllib3.request

try:
    urllib.request.urlopen("https://www.facebook.com")
except:
    print("Consegui acessar o Facebook")
else:
    print("Não consegui acessar o Facebook")