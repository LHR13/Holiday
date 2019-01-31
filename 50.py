k=eval(input("请输入旋转的次数"))
n=input("请输入一组数字：")
l=[]
for i in n:
    l.append(i)

s=1
while s<=k:
    a=l[-1]
    l.pop()
    l.insert(0,a)
    s+=1
print(l)
