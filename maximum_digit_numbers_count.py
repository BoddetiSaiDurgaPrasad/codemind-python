n=int(input())
c=list(map(int,input().split()))
h=0
for i in range(n):
    k=len(str(c[i]))
    if(h<k):
        h=k
v=[]
for i in range(n):
    if(len(str(c[i]))==h):
        v.append(c[i])
print(*v)