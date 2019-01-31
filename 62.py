n=input("请输入一个数组：")
a=n[0]
Max=0
Min=n[0]
for i in n:
   if int(Max)<int(i):
       Max=i
for r in n:
    if int(Min)>int(r):
        Min=r
l=[]
c=n.find(Max)
g=n.find(Min)
for p in n:
    l.append(p)
l[0],l[c]=l[c],l[0]
l[-1],l[g]=l[g],l[-1]
print(l)
