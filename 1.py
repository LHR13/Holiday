A=[1,2,3,4]
n=0
for f in A:
    for s in A:
        for t in A:
            if f!=s and f!=t and s!=t:
                n+=1
                p=100*f+10*s+t
                print(p,end=" ")
print("\n符合题意的数总共有%d"%n)
            
