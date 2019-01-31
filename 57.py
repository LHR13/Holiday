def transfor(fun):   #定义一个转换函数，
    def war(N):  #带参数的装饰器，把参数传闭包里
        L = N.copy()
        for j in range(len(L)):
            temp = str(L[j])
            L[j] = temp
        l = ' '.join(L).center(90)
        fun(l)
    return war
@transfor   #甜甜的函数糖
def f1(N):    #把print定义成f1()函数
    print(N)
 
N = [1]
for i in range(10):
    f1(N)   #这里注意要用f()代替print()
    N.append(0)
    N = [N[k] + N[k-1] for k in range(i+2)]
