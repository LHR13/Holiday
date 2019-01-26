n=eval(input("请输入要分解的数："))
t=n
i=2
l=[]
while i<=n:
    if n%i==0:
        l.append(i)
        n=n//i
    else:
        i+=1
k=[]
for p in l:
    q=str(p)
    k.append(q)
print("%d="%t+'*'.join(k))
