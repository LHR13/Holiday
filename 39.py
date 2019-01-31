n=2
c=0
while n<=100:
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    if flag==1:
        print(n,end=" ")
        c+=1
    n+=1
