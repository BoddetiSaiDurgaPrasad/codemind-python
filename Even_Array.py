n=int(input())
c=0
k=list(map(int,input().split()))
for i in range(n):
    if(k[i]%2==0):
        c+=1
if(c==n):
    print("True")
else:
    print("False")