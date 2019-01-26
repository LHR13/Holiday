s=input("请输入一串字符：")
letter=0
space=0
num=0
other=0
for i in s:
    if i>="a"and i<="z":
        letter+=1
    elif i==" ":
        space+=1
    elif isinstance(i,int):
        num+=1
    else:
        other+=1
print("字符串里有%d个字母,%d个空格，%d个数字，%d个其他字符"%\
      (letter,space,num,other))
