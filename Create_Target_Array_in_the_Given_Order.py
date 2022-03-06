n=int(input())
s=list(map(int,input().split()))
k=int(input())
c=[]
m=list(map(int,input().split()))
for i in range(n):
    c.insert(m[i],s[i])
print(*c)