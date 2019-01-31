import random
temp=""
for i in range(4):
    c= random.randint(1, 3)  
    if c==1:                 
        temp+=random.choice('0123456789')
    elif c==2:               
        num=random.randint(65, 90)
        temp+=chr(num)
    elif c==3:               
        num=random.randint(97, 122)
        temp+=chr(num)
print(temp)
