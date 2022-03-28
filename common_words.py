n=input()
s=input()
n=n.lower()
s=s.lower()
#print(n,s)
n=n.split()
s=s.split()
k=n+s
k=set(s)
k=list(s)
c=[]
for i in range(len(k)):
    if(s.count(k[i])>=1 and n.count(k[i])>=1):
        c.append(k[i])
c=" ".join(c)
print(c)