def plural (n, a,b,c):
    if n%10 == 1 and n%100!=11:
        k = (str(n)+' '+ a)
    elif (n%10 == 2 or n%10 == 3 or n%10 == 4) and (n%100 != 12 and n%100 != 13 and n%100 != 14):
        k = (str(n) + ' ' + b)
    else:
        k = (str(n) + ' ' + c)
    print(k)
s = input()
n = int(input())
if s == 'утюг':
    plural(n, 'утюг', 'утюга', 'утюгов')
elif s == 'ложка':
    plural(n, 'ложка', 'ложки', 'ложек')
elif s == 'гармошка':
    plural(n, 'гармошка', 'гармошки', 'гармошек')
else:
    plural(n, 'чайник', 'чайника', 'чайников')

