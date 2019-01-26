def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        n=f(n-1)+f(n-2)
        return n
