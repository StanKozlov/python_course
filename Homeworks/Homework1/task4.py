s= input()
s=s.lower()
d = dict()
l = []
for i in s:
    l.append(i)
    d[i] = 0
for i in l:
    for key in d:
        if key == i:
            d[i] += 1
keys = d.keys()
keys = list(keys)
keys.sort()
for i in keys:
    print(i + ' ' + str(d[i]))
