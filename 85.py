n=(1,2,3,4,5,4,3,2,1)
m=list(n)
for i in m:
    s=m.count(i)
    if s==1:
        print(i)
