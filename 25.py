def f(n):
    if n==1:
        return 1
    else:
        s=f(n-1)+1
        return s*2
        
