y,m,d=eval(input("请输入年月日数字，中间用逗号隔开："))
if y>=0 and m>=1 and m<=12 and d>=1 and d<=31:
    if y%100==0 or y%4==0:
        a=[0,31,60,91,121,152,182,213,244,274,305,335,366]
        n=a[m-1]+d
        print("这是这一年的第%d天"%n)
    else:
        a=[0,31,59,90,120,151,181,212,243,273,304,334,365]
        n=a[m-1]+d
        print("这是这一年的第%d天"%n)
else:
    print("数据输入错误！")

