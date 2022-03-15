n=int(input())
k=list(map(int,input().split()))
z=0
for i in range(len(k)):
    z+=k[i]
print(z)