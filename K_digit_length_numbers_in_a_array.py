a,b=map(int,input().split())
s=list(map(int,input().split()))
c=0
#print(s,b)
for i in range(a):
    s[i]=abs(s[i])
    if(len(str(s[i]))==b):
        c+=1
print(c)