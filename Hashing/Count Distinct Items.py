l = [1,2,1,3,3,2,4,2,6,3,8,9,1]
n = []
for i in l:
    if i not in n:
        n.append(i)
    else:
        pass
print(n)

print(set(l))