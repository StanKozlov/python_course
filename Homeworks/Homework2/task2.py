def prime(p):
    i = 2
    j = True
    if p == 1:
        return 'False'
    elif p == 2:
        return 'True'
    else:
        while i*i <= p and j != False:
            if p % i == 0:
                j = False
            i += 1
        if j == True:
            return 'True'
        else:
            return 'False'
Quantity = int(input())
for i in range(Quantity):
    n = int(input())
    print(prime(n))


