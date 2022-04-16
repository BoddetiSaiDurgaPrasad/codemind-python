n=int(input())
k=list(map(int,input().split()))
for i in range(len(k)):
    if(i==len(k)-1):
        k[i]=-1
    else:
        c=0
        for j in range(i+1,len(k)):
            if(c<k[j]):
                c=k[j]
        k[i]=c
print(*k)