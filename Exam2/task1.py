import re

with open('hp5.txt', 'r') as f:
    data = str(f.read()).split('\n')

count = {}
for i in data:
    ids1 = re.findall('((\w+\s\w+) whispered)', i)
    ids2 = re.findall('(whispered (\w+\s\w+))', i)
    ids3 = re.findall('((\w+) whispered)', i)
    ids4 = re.findall('(whispered (\w+))', i)
    
    if ids1 != []:
        if str(ids1[0][1])[0].isupper() == True and str(str(ids1[0][1]).split(' ')[1])[0].isupper() == True:
            if ids1[0][1] not in count:
                count[ids1[0][1]] = 1
            else:
                count[ids1[0][1]] +=1

    if ids2 != []:
        if str(ids2[0][1])[0].isupper() == True and str(str(ids2[0][1]).split(' ')[1])[0].isupper() == True:
            if ids2[0][1] not in count:
                count[ids2[0][1]] = 1
            else:
                count[ids2[0][1]] +=1


    if ids3 != []:
        if str(ids3[0][1])[0].isupper() == True:
            if ids3[0][1] not in count:
                count[ids3[0][1]] = 1
            else:
                count[ids3[0][1]] +=1

    if ids4 != []:
        if str(ids4[0][1])[0].isupper() == True:
            if ids4[0][1] not in count:
                count[ids4[0][1]] = 1
            else:
                count[ids4[0][1]] +=1
       
maximal = 0
for i in count:
    if count[i] > maximal:
        maximal = count[i]
for i in count:
    if count[i] == maximal:
        print(str(maximal) + ' ' + str(i))
