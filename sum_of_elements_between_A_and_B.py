n=int(input())
c=0
k=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(len(k)):
    if(a<=k[i] and k[i]<=b):
        c+=k[i]
print(c)