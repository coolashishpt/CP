arr = [61, 14, 75, 71, 36, 34, 12]
sum = 68

c = 0
for i in range(len(arr)):
    if arr[i] < sum:
        v = sum - arr[i]
        if v in (arr[:i] + arr[i+1:]):
            c += 1
            break

if c == 1:
    print("Yes")

else:
    print("No")
