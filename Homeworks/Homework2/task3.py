def euclid(n, m):
    if n%m == 0:
        return m
    else:
        return euclid (m, n%m)
s = input()
numbers = s.split(" ")
lst = []
for i in numbers:    
    lst.append(int(i))
print(euclid(lst[0], lst[1]))
