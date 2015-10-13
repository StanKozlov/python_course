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
    if lst == []:
        return None
    else:
        return lst


s = input()
numbers = s.split(" ")
list_of_interest = []
for i in numbers:
    list_of_interest.append(int(i))
results = rpfilter(*list_of_interest)   
if results is not None:
    for i in results:
        print(i, end = ' ')
else:
    print(results)
    




