n=int(input("请输入总人数（从一个报数开始以1编号，逐次递增）："))
a=list(range(1,n+1))
while len(a)>2:
    c = len(a) % 3
    b = []
    if c == 0:
        for i in range(1, len(a) + 1):
            if i % 3 != 0:
                b.append(a[i - 1])
        a = b
        print(a)
    else:
        for i in range(1, len(a) + 1):
            if i % 3 != 0:
                b.append(a[i - 1])
        a = b[-c:] + b[:-c]
        print(b)
        print(a)
print(a)
print("最后剩下人的原始编号为：{}".format(a[1]))
