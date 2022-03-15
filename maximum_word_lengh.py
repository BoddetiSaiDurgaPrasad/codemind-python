n=input()
k=n.split()
for i in range(len(k)):
    c=k[i]
    x=len(c)
    k[i]=x
print(max(k))