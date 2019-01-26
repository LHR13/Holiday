try:
    a=eval(input("请输入一个无符号的整数"))
    import math
    b=math.log(a,3)
    c=int(b)
    if 3**c==a:
        print("这个数是3的幂次方！")
    else:
        print("这个数不是3的幂次方！")
except:
    print("数据输入错误！")
