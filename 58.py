try:
    m=input("请输入一个字符串")
    n=input("请输入要搜寻的子字符串")
    print(m.index(n))
except:
    print("子字符串不在原字符串中！")
