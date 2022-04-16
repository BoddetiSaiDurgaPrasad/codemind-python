n=input()
n=n.lower()
k=[]
for i in range(len(n)):
    if(n.count(n[i])==1 and n[i]!=" "):
        k.append(n[i])
k.sort()
k="".join(k)
print(k)