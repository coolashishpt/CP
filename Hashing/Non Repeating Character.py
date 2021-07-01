s = "hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs"

count = [0] * 256
for i in s:
    count[ord(i)] += 1

for j in s:
    if count[ord(j)] == 1:
        print(j)
        break

# print(count[ord("h")])