def prime(potential_victim):
    i = 2
    flag = True
    if potential_victim == 1:
        return False
    elif potential_victim == 2:
        return True
    else:
        while i*i <= potential_victim and flag is not False:
            if potential_victim % i == 0:
                flag = False
            i += 1
        return flag
Quantity = int(input())
for i in range(Quantity):
    candidate = int(input())
    print(prime(candidate))


