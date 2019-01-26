a=eval(input("请输入相加的基数："))
n=eval(input("请输入相加的位数："))
s=0
i=0
sum=0
while i<n:
    s+=a*(10**i)
    i+=1
    sum+=s
print(sum)

