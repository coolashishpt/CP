def validate(s):
    #your code here
    n = "1234567890"
    p = "@#$-*"
    u = "QWERTYUIOPASDFGHJKLZXCVBNM"
    l = "qwertyuiopasdfghjklzxcvbnm"
    print(len(s))
    if len(s) >= 10:
        c = 0
        for i in s:
            if (i in n) or (i in p) or (i in u) or (i in l):
                c += 1
        print(c)
        if c == len(s):
            return 1
        else:
            return 0
    else:
        return 0


print(validate("OoD7JsCsRyRo"))