l=eval(input("请输入整数，中间用逗号隔开："))
m=eval(input("请输入m的值："))
k=list(l)
r=0
k.reverse()
for i in k:
    k.remove(i)
    r+=1
    if r==m:
        break
k.reverse()
n=[]
for p in k:
    n.append(p)
    if len(n)==m:
        break
s=1
while s<=m:
    a=k[-1]
    k.pop()
    k.insert(0,a)
    s+=1
for q in n:
    k.append(q)
print(k)
