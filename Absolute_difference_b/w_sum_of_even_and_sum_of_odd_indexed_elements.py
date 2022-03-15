n=int(input())
k=list(map(int,input().split()))
c,z=0,0
for i in range(len(k)):
    if(i%2==0):
        c+=k[i]
    else:
        z+=k[i]
print(abs(c-z))