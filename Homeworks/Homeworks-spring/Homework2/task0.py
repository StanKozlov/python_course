result = []

if issubclass(D, A) is True:
    result.append('A')
if issubclass(D, B) is True :
    result.append('B')
if issubclass(D, C) is True:
    result.append('C')

result = sorted(result)
s = ''
for i in result:
    s += i + ' '
print(s)
