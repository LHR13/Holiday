string = ['a','b','c','d','\n']
def Permutation(string,i):
    if string == None:
        return
    if string[i] == '\n':
        print("%s\n"%string)
    else:
        for j in range(i,len(string)-1):            
            string[j],string[i] = string[i],string[j]
            Permutation(string,i+1)
            string[j],string[i] = string[i],string[j]
Permutation(string,0)     
