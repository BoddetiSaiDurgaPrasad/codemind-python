n=int(input())
k=list(map(int,input().split()))
c=[]
#print(k)
for i in range(n):
    if k[i] not in c:
        c.append(k[i])
print(*c)