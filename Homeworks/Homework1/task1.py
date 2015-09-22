s=input()
n=int(input())
if n%10 == 1 and n%100!=11:
    print(str(n)+' '+s)
elif (n%10 == 2 or n%10 == 3 or n%10 == 4) and (n%100 != 12 and n%100 != 13 and n%100 != 14):
    if s == 'утюг':
        print(str(n) + ' ' + 'утюга')
    else:
        print(str(n) + ' ' + 'ложки')
else:
    if s == 'утюг':
        print(str(n) + ' ' + 'утюгов')
    else:
        print(str(n) + ' ' + 'ложек')
