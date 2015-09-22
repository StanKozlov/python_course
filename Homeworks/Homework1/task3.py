s = input()
numbers =(s.split(' '))
num = []
for i in numbers:
    num.append(int(i))
lst1 = num[::2]
lst2 = num[1::2]
lst1.sort()
lst2.sort(reverse = True)
lst3 = []
i = 0
k = max(len(lst1), len(lst2))
while i <= k-2:
    lst3.append(lst1[i])
    lst3.append(lst2[i])
    i += 1
if len(lst1)>len(lst2):
    lst3.append(lst1[i])
elif len(lst2)>len(lst1):
    lst3.append(lst2[i])
else:
    lst3.append(lst1[i])
    lst3.append(lst2[i])
str1 = ''
for i in lst3:
    str1 += str(i) + ' '
print (str1)
