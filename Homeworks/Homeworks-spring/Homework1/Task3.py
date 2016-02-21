n = int(input())
functions = input().split(' ')
index = n-1
working_list = {}
m = int(input())

for k in range(m):
    s = input().split(' ')
    if s[0] not in working_list:
        working_list[s[0]] = {s[1]: s[2]}
    else:
        working_list[s[0]].update({s[1]: s[2]})   
exc = input()


def function_killer2(index, exc):
    s = ''
    if exc in working_list[functions[index]] and working_list[functions[index]][exc] == '_':
        for j in functions[:index + 1]:
            s += j + ' '
        return s
    else:
        if exc in working_list[functions[index]]:
            exc2 = working_list[functions[index]][exc]
            exc = exc2
        else:
            pass
        index = index - 1
        if index != -1:
            return function_killer2(index, exc)
        else:
            return ''
              
print(function_killer2(index, exc))


            
            
            

    

    
