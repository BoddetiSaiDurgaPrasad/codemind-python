n=input()
n=n.lower()
k=n.split()
ca=0
for i in range(len(k)):
    c=k[i]
    if(c[0]=="a" or c[0]=="e" or c[0]=="i" or c[0]=="o" or c[0]=="u"):
        if(c[-1]!="a" or c[-1]!="e" or c[-1]!="i" or c[-1]!="o" or c[-1]!="u"):
            ca+=1
print(ca)