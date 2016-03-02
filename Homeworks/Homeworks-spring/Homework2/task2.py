n = int(input())
classes = {}
checked = []
methods = {}

for i in range(n):
    s = input().split(' : ')
    if len(s) == 1:
        classes[s[0]] = []
    else:
        progenitors = s[1].split(' ') 
        classes[s[0]] = progenitors

m = int(input())
for j in range(m):
    s1 = input().split(' ')
    if s1[0] not in methods:
        methods[s1[0]] = [s1[1]]
    else:
        methods[s1[0]].append(s1[1])
print(methods)

            
def mf(b, k):
    if k in methods[b]:
        return b
    if b in checked:
        return None
    checked.append(b)
    for i in classes[b]:
        if i not in checked:
            return mf(i, k)
    
                
question = input().split(' ')
print(mf(question[0], question[1]))
