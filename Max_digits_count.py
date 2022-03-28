n=int(input())
s=list(map(int,input().split()))
for i in range(n):
    s[i]=len(str(s[i]))
a=max(s)
print(s.count(a))