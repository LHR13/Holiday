n=1
while True:
    s=(3125*n+2101)/256
    if s/int(s)==1:
        break
    else:
        n+=1
b=int(s)
print("原来最少有%d个桃子"%b)
