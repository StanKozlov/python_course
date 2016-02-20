import urllib
import json
import pickle
from urllib.request import urlopen

with open('interactors_Nikita.txt', 'r') as f:
    data = str(f.read()).split('\n')
protein = {}
for word in data:
    k = word.split(',,')
    if k != [] and k[0] != '':
        name = list(k[0].split(':'))[1][1:]
        print(name)
        protein[name] = word
print(protein)
protein2 = {}
for elt in protein:
    aqua = protein[elt].split(',, ')
    dict = {}
    for i in aqua:
        quack = i.split(': ')
        print(quack)
        if quack != [] and quack[0] != '':
            dict[quack[0]] = quack[1]
    print(type(dict))
    protein2[str(dict['string_id']).replace(', Uniprot record is missing', '')] = dict
print(protein2)


url = 'http://string-db.org/api/tsv-no-header/abstracts?identifier=APP&species=9606&required_score=400&limit=3000'
q = urllib.request.urlopen(url)
s1 = str(q.read()).replace("b'", '').replace('\\n', ' ').split(' ')
pmidAPP = s1
print(pmidAPP)
with open('data_string_tsv_thursday.txt','w') as f:
    for protein in protein2:
        if protein != 'ENSP00000284981':
            url = 'http://string-db.org/api/tsv-no-header/abstracts?identifier='+protein+'&species=9606&required_score=400&limit=3000'
            try:
                q = urllib.request.urlopen(url)
            except urllib.request.HTTPError as err:
                print(err.code)
            s1 = str(q.read()).replace("b'", '').replace('\\n', ' ').split(' ')
            s2 = ''
            for id in s1:
                if id in pmidAPP:
                    s2 += id + '\t'
                    print(s2)
            if s2 != '':
                print(s2)
                f.write(protein + '\t' + s2 + '\n')
