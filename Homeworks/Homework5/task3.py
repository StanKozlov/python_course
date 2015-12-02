import re
import sys
code = sys.stdin.read()
data = code.split('\n')
i = 1
for s in data:
    ids = re.findall("((\w+) = )", s)
    if ids != []:
        print(str(i) + ' ' + ids[0][1])
    i += 1

    

