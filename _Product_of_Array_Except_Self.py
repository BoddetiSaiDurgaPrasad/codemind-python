n=int(input())
z=[]
k=list(map(int,input().split()))
for i in range(len(k)):
    c=k.copy()
    del c[i]
    h=1
    for j in range(len(c)):
        h*=c[j]
    z.append(h)
print(*z)