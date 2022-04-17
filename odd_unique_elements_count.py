n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(len(s)):
    if(s.count(s[i])==1 and s[i]%2!=0):
        c+=1
print(c)