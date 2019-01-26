def f(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

p=0
for i in range(1,21):
    p+=f(i)
print(p)


        
