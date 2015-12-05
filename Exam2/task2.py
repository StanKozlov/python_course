
import requests
import re

links = []
with open('links.txt', 'r') as f:
    quack = str(f.read()).split('\n')
    for line in quack:
        if line != '':
            url = line
            data = requests.get(url).text
            ids1 = re.findall('(\w+@\w+.{0,1}\w*)', data)
            ids2 = re.findall('(\w+.\w+@\w+.\w+)', data)
            if ids1 != []:
                links.append(ids1[0])
            if ids2 != []:
                links.append(ids2[0])

with open('email_addresses.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')

