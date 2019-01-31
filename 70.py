def f(n):
    if n%2==0:
        l=[]
        for i in range(2,n+1):
            if i%2==0:
                l.append(i)
    else:
        l=[]
        for p in range(1,n+1):
            if p%2!=0:
                l.append(p)
    s=0
    for t in l:
        s+=(1/t)
    return print(s)

