n=int(input())
c=0
k=list(map(int,input().split()))
for i in range(n):
    if(i==0 or i==n-1):
        continue
    else:
        if(k[i+1]%2!=0 and k[i-1]%2==0) or (k[i+1]%2==0 and k[i-1]%2!=0):
            c+=1
print(c)