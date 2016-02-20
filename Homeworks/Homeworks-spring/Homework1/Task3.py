n = int(input())
functions = input().split(' ')
functions.reverse()
working_list = {}
m = int(input())

for i in range(m):
    s = input().split(' ')
    if s[0] not in working_list:
        working_list[s[0]] = {s[1]: s[2]}
    else:
        working_list[s[0]].update({s[1]: s[2]})   
exc = input()


def function_killer(fun, exc):
    s = ''
    if functions != []:
        if fun in working_list:
            if exc in working_list[fun]:
                if working_list[fun][exc] != '_':
                    exc2 = working_list[fun][exc]
                    functions.remove(functions[0])
                    if functions != []:
                        fun = functions[0]
                        return function_killer(fun, exc2)
                    else:
                        return ''
                else:
                    functions.reverse()
                    for i in functions:
                        s += i + ' '
                    return s
            else:
                functions.remove(functions[0])
                if functions != []:
                    fun = functions[0]
                    return function_killer(fun, exc)
                else:
                    return ''
        else:
            functions.remove(functions[0])
            if functions != []:
                fun = functions[0]
                return function_killer(fun, exc)
            else:
                return ''
    else:
        return ''

print(function_killer(functions[0], exc))

            
            
            

    

    
