n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(n):
    if(i==0 or i==n-1):
        continue
    else:
        if(k[i]%2==0):
            if(k[i+1]%2!=0 and k[i-1]%2!=0):
                c+=1
print(c)