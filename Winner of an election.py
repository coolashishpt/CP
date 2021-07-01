arr = ["john","johnny","jackie","johnny","john",
       "jackie","jamie","jamie","john","johnny","jamie",
       "johnny","john"]

d = {}
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
m = max(d.values())
print(m)

d1 = {}
for i in d:
    if d[i] == m:
        d1[i] = d[i]

print(d1)
s = sorted(d1)[0]

l = []
l.append(s)
l.append(m)


print(l)
