foA.open("A","w+")
foB.open("B","w+")
foC.open("C","wt")
s=list(foA.read())
p=list(foB.read())
q=s+p
q.sort()
foC.write(q)

