n=int(input())
k=list(map(int,input().split()))
for i in range(len(k)):
    if(k[i]%2!=0):
        c=i
print(c)