n=int(input())
s=list(map(int,input().split()))
c=int(input())
h=0
for i in range(c):
    h+=s[i]
print(h)