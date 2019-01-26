def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

def g(n):
    return f(n+2)/f(n+1)

x=0
for i in range(1,21):
    x+=g(i)
print(x)
