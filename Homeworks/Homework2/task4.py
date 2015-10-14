def euclid(n, m):
    if n % m == 0:
        return m
    else:
        return euclid(m, n % m)


def rpfilter(a, *args):
    lst = []
    for arg in args:
        if euclid(a, arg) == 1:
            lst.append(arg)
    return lst


s = input()
numbers = s.split(" ")
list_of_interest = []
for i in numbers:
    list_of_interest.append(int(i))
if rpfilter(*list_of_interest) != []:   
    for i in rpfilter(*list_of_interest):
        print(i, end = ' ')
else:
    print('None')
    




