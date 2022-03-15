n=int(input())
c,z=0,0
k=list(map(int,input().split()))
for i in range(len(k)):
    if(k[i]%2==0):
        c+=k[i]
    else:
        z+=k[i]
print(abs(c-z))