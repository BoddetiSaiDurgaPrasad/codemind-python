k=[True]*(1000000)
def isprime():
    k[0]=k[1]=False
    for i in range(2,len(k)):
        if(k[i]==True):
            k[i]=i
            hi=1
            for j in range(i,len(k),i*hi):
                if(j==i):
                    k[j]=True
                elif(k[j]==True):
                    k[j]=False
                hi+=1
isprime()
c=0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(k[i]==True):
        c+=1
print(c)
