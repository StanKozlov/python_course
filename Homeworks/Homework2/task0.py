def plural (n, a,b,c):
    if n%10 == 1 and n%100!=11:
        k = str(n)+' '+ a
    elif (n%10 == 2 or n%10 == 3 or n%10 == 4) and (n%100 != 12 and n%100 != 13 and n%100 != 14):
        k = str(n) + ' ' + b
    else:
        k = str(n) + ' ' + c
    return k
s = input()
n = int(input())
if s == 'утюг':
    m = plural(n, 'утюг', 'утюга', 'утюгов')
elif s == 'ложка':
    m = plural(n, 'ложка', 'ложки', 'ложек')
elif s == 'гармошка':
    m = plural(n, 'гармошка', 'гармошки', 'гармошек')
else:
    m = plural(n, 'чайник', 'чайника', 'чайников')
print(m)

