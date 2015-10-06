def euclid(n, m):
    if n%m == 0:
        return m
    else:
        return euclid (m, n%m)
def rpfilter(a, args):
    lst = []
    for arg in args:
        if a > int(arg):
            k = euclid(a, arg)
            if k == 1:
                lst.append(str(arg))
        else:
            k = euclid(arg, a)
            if k == 1:
                lst.append(str(arg))
    if lst == []:
        return 'None'
    else:
        return ' '.join(lst)
s = input()
numbers = s.split(" ")
lst1 = []
i = 1
a = int(numbers[0])
while i <= (len(numbers) - 1):    
    lst1.append(int(numbers[i]))
    i += 1
print(rpfilter(a, lst1))



