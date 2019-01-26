def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

n=eval(input("请输入项数："))
print(f(n))
