import re
import sys
data = sys.stdin.read()
pattern = "\W+"
result = re.sub(pattern, " ", data)
print(result)
