n = int(input())
dic = {}
checked = []

for i in range(n):
    s = input().split(' : ')
    if len(s) == 1:
        dic[s[0]] = []
    else:
        progenitors = s[1].split(' ')
        dic[s[0]] = progenitors


def dfs(b):
    if b in checked:
        return True
    checked.append(b)
    for i in dic[b]:
        if i not in checked:
            dfs(i)

m = int(input())
for j in range(m):
    s1 = input().split(' ')
    dfs(s1[1])
    if s1[0] in checked:
        print('Yes')
    else:
        print('No')
    checked = []

    
