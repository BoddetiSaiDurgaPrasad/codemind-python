n=input()
n==n.lower()
s=n.split()
for i in range(len(s)):
    c=s[i]
    k=0
    for j in range(len(c)):
        if(c[j]=="a" or c[j]=="e" or c[j]=="i" or c[j]=="o" or c[j]=="u"):
            k+=1
    print(k,end=" ")