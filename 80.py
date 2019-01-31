mt=eval(input("请输入一个数组，每个数之间用逗号分隔："))
m=list(mt)
for i in m:
    if i==0:
        m.remove(i)
        m.append(i)
n=tuple(m)
print(n)
