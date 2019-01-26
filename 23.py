for n in range(2,1001):
    t=n
    i=2
    l=[1]
    p=0
    while i<=n:
        if n%i==0:
            l.append(i)
            i+=1
        else:
            i+=1
    for s in l:
        p+=s
        if p==t:
            print(t)
                
    
