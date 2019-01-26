jia=['c','b','a']
yi=['x','y','z']
for i in jia:
    for p in yi:
        if i=="c":
            if p=="y":
                print(i+" VS "+p)
                yi.remove(p)
        elif i=="a":
            if p!="y":
                print(i+" VS "+p)
        elif i=="b":
            print(i+" VS "+p)
            yi.remove(p)
            break
        else:
            pass
        
