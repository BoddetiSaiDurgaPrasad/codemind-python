n=int(input())
s=list(map(int,input().split()))
c=0
a=set(s)
a=list(a)
for i in range(len(a)):
    if(a[i]==s.count(a[i])):
        c+=1
print(c)
