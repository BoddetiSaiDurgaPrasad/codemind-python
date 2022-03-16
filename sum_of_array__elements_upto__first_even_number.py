n=int(input())
h=0
s=list(map(int,input().split()))
for i in range(n):
    if(s[i]%2==0):
        break
    else:
        h+=s[i]
print(h)