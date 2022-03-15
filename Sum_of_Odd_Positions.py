n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(len(k)):
    if(i%2!=0):
        c+=k[i]
print(c)