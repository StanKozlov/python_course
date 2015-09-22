str1 = input()
lst = []
numbers = str1.split(" ")
for i in numbers:    
    lst.append(int(i))
mean_value = sum(lst)/(len(lst))
print(mean_value)
