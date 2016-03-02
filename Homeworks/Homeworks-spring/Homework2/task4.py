n = int(input())
dic = {}
checked = []
exceptions = []
result = []

for i in range(n):
    s = input().split(' : ')
    if len(s) == 1:
        dic[s[0]] = []
    else:
        progenitors = s[1].split(' ') 
        dic[s[0]] = progenitors


def dfs(b):
    if b in checked:
        return False
    checked.append(b)
    for i in dic[b]:
        if i not in checked:
            dfs(i)
        
m = int(input())
for j in range(m):
    k = input()
    dfs(k)
    for i in checked:
        if i in exceptions:
            result.append(k)
            break
    exceptions.append(k)
    checked = []
for i in result:
    print(i)
