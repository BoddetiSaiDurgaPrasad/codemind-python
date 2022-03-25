n=int(input())
k=list(map(int,input().split()))
#print(*k)
for i in range(len(k)):
    if(k[i]<0):
        k[i]=k[i]*-1
    c=str(k[i])
    print(len(c),end=" ")