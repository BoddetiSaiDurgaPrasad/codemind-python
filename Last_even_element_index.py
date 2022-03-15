n=int(input())
d=list(map(int,input().split()))
for i in range(len(d)):
    if(d[i]%2==0):
        c=i
print(c)