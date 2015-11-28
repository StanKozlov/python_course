import sys
import re
data = sys.stdin.read()
results = re.findall("[Yy]ou", data)
count = 0
for i in results:
    count += 1
print(count)
