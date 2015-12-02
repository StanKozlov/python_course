import re
import sys
code = sys.stdin.read()
data = code.split('\n')
i = 1
for s in data:
    ids = re.match(' *([\w,. ]+) = ', s)
    result = ''
    if ids != None:
        groups = list(ids.groups())
        for group in groups:
            quack = group.split(',')
            for word in quack:
                result += str(word)           
            print(i, result)
    i +=1
        
