n=input()
k=n.split()
c=[]
for i in range(len(k)):
    h=k[i]
    c1=min(h)
    c2=max(h)
    c.append(c1)
    c.append(c2)
print(*c)