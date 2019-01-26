import math
for n in range(10000):
    b=n+100
    m=math.sqrt(b)
    v=b+168
    c=math.sqrt(v)
    x=round(m)
    z=round(c)
    if x*x==b and z*z==v:
        print(n)        

        
