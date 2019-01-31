def f(n):
    if n=="":
        return n
    else:
        s=f(n[1:])+n[0]
        return s
l=input("请输入一串字符：")
print(f(l))
