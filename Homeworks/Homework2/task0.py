def plural(n, *args):
    if n % 10 == 1 and n % 100 != 11:
        word = args[0]
    elif (1 < n % 10 < 5) and (n % 100 not in (12, 13, 14)):
        word = args[1]
    else:
        word = args[2]
    return word
string = input()
number = int(input())
if string == 'утюг':
    proper_word = plural(number, 'утюг', 'утюга', 'утюгов')
elif string == 'ложка':
    proper_word = plural(number, 'ложка', 'ложки', 'ложек')
elif string == 'гармошка':
    proper_word = plural(number, 'гармошка', 'гармошки', 'гармошек')
else:
    proper_word = plural(number, 'чайник', 'чайника', 'чайников')
print("%d %s" % (number, proper_word))

