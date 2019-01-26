l=[int(n) for n in eval(input("请输入一组数，中间用逗号隔开："))]
b=set(l)
c=list(b)
if l==c:
    print("False")
else:
    print("True")
