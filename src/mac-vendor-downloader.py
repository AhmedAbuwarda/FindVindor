import requests

r = requests.get('http://standards-oui.ieee.org/oui.txt')
with open('oui.txt','wb') as f:
    f.write(r.content)
