try:
    i=eval(input("请输入当月的利润（单位：元）："))
    if type(i) is int or type(i)is float:
        if i<=100000:
            n=i*0.1
        elif i>100000 and i<=200000:
            n=10000+(i-100000)*0.075
        elif i>200000 and i<=400000:
            n=17500+(i-200000)*0.05
        elif i>400000 and i<=600000:
            n=27500+(i-400000)*0.03
        elif i>600000 and i<=1000000:
            n=33500+(i-600000)*0.015
        else:
            n=39500+(i-1000000)*0.01
        print("本月应发放的奖金总数为{:.2f}元".format(n))
except:
    print("输入错误！")


