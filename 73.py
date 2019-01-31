mt=eval(input("请输入一个数组，每个数之间用逗号分隔："))
n=eval(input("请输入目标值："))
m=list(mt)
for i in range(0,len(m)+1):
    for p in range(i+1,len(m)):
        if m[i]+m[p]==n:
            print("下标%d，和下标%d"%(i,p))
            
