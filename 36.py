week=input("请输入星期的英文名（首字母大写）：")
if week[0]=="M":
    print("今天是星期一")
elif week[0]=="W":
    print("今天是星期三")
elif week[0]=="F":
    print("今天是星期五")
elif week[0]=="T":
    if week[1]=="u":
        print("今天是星期二")
    if week[1]=="h":
        print("今天是星期四")
elif week[0]=="S":
    if week[1]=="a":
        print("今天是星期六")
    if week[1]=="u":
        print("今天是星期日")
