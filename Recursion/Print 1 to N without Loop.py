def fun(n):
    if n > 0:
        fun(n-1)
        print(n)
    return
fun(64)