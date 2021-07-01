def check(l):
    if 0 in l:
        return True
    else:
        for i in range(len(l)):
            c = l[i]
            for j in range(i + 1, len(l)):
                # print(i, j)
                c = c + l[j]

                if c == 0:
                    return True

        else:
            return False

def iszerosum(l):
    pre_sum = 0
    h = set()
    for i in range(len(l)):
        pre_sum += l[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False


print(iszerosum([-1, 4, -3, 5, 1]))
print(check([1, 4, 13, -3, -10, 5]))
print(check([3, 1, -2, 5, 6]))
print(check([5, 6, 0, 8]))
