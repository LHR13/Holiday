def f(n):
    a=bin(n)
    s=0
    for i in a:
        if i=="1":
            s+=1
    print(s)
