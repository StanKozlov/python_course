P = [['Ah','Bt'], ['Bh','Ct'], ['Ch','At'], ['Dh','Eh'], ['Et','Ft'], ['Fh','Dt']] #first inputed genome
Q = [['Bt','Ah'], ['Bh','Et'], ['Eh','Fh'], ['Ft','At'], ['Ch','Dh'], ['Ct','Dt']] #second inputed genome
genes = [['Ah','At'], ['Bh','Bt'], ['Ch', 'Ct'], ['Dh', 'Dt'], ['Eh', 'Et'], ['Fh', 'Ft']] #genes
Z = P + Q #it is a breakpoint graph

##for i in P:
##    if i in Q or list(reversed(i)) in Q:
##        print(i)
##        BPG.append(i)
##        BPG.append(list(reversed(i)))
##    else:
##        if i not in BPG or list(reversed(i)) not in BPG:
##            BPG.append(i)
##        for j in i:
##            for k in Q:
##                if (j in k) and (k not in BPG):
##                    BPG.append(k)
##                    break
##print(BPG)


vertices = ['At', 'Ah', 'Bt', 'Bh', 'Ct', 'Ch', 'Dt', 'Dh', 'Et', 'Eh', 'Ft', 'Fh']       
names = {}
i = 0
for name in vertices:
    names[i] = name
    print(names[i], i)
    i += 1
    
#BPG as a matrix
BPG = [[0 for l in range(len(names))] for m in range(len(names))]    

count_degree = [0 for i in range(len(names))]

for h in names:
    for v in names:
        if ([names[h], names[v]]) in Z or list(reversed([names[h], names[v]])) in Z:
            BPG[h][v] = 1
            count_degree[h] += 1
        else:
            BPG[h][v] = 0

for i in BPG:
    print(str(i) + '\n')

#analysis of BPG
ex = []
cycles = 0
pathes = 0


def dfs(node):
    print(str(names[node]) + ' ' + str(count_degree[node]))
    ex.append(node)
    for i in names:
        if BPG[node][i] == 1 and i not in ex:
            dfs(i)
            if count_degree[i] == 1 and count_degree[node] == 2:
                return True
            # only 2 or 1 by definition. If both == 1,
            # then it is cycle with only two elements in it
          
for i in names:
    if i not in ex:
        if dfs(i):
            print('Path')
            pathes += 1
        else:
            print('Cycle')
            cycles += 1

print('Here are ' + str(cycles) + ' cycles, and ' + str(pathes) + ' pathes') 
    
