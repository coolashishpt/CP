

def check_pal_per(a):
    l = []

    for i in set(a):
        n = a.count(i)
        if n % 2 == 0:
            l.append(n)
        elif n % 2 == 1:
            l.append(n)

    if l.count(1) > 1:
        return False
    else:
        return True

print(check_pal_per("abba"))
print(check_pal_per("acbccab"))
print(check_pal_per("abcc"))
print(check_pal_per("ab"))
print(check_pal_per("geeksgeeks"))
