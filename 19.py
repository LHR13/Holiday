b=input("请输入32位无符号整数：")
s=eval(b)
if len(b)==32:
    a=bin(s)
    l=[]
    for i in a:
        l.append(i)
    l.reverse()
    print(l)
else:
    print("数据输入错误！")
