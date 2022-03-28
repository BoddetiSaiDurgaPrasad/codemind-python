n=int(input())
s=list(map(int,input().split()))
#print(s)
for i in range(len(s)):
    s[i]=len(str(s[i]))
k=min(s)
print(s.count(k))