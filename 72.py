s=input("请输入一段元素类型相同的字符串（字母或数字）：")
l=[]
for i in s:
    l.append(i)
l.sort()
m="".join(l)
print(m)
