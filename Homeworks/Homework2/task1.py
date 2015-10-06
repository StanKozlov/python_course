def combinations(n,k):
    if k > n:
        return 0
    elif (n == k or k == 0):
        return 1
    else:
        return combinations(n-1, k-1) + combinations(n-1, k)
s = input()
numbers = s.split(" ")
lst = []
for i in numbers:    
    lst.append(int(i))
print(combinations(lst[0], lst[1]))

