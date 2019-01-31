n=eval(input("请输入一个非负整数："))
c=0
s=2
while s<n:
    flag=1
    for i in range(2,s):
        if s%i==0:
            flag=0
            break
    if flag==1:
        c+=1
    s+=1
print("共有%d个小于此数的质数"%c)
    
        
