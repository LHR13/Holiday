mt=eval(input("请输入一个密码，每个数之间用逗号分隔："))
m=list(mt)
l=[]
for i in m:
    s=(i+5)%10
    print(s)
    l.append(s)
l[0],l[3]=l[3],l[0]
l[1],l[2]=l[2],l[1]
n=tuple(l)
print(n)
