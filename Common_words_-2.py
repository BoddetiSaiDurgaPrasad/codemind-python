s=input()
c=0
s=s.split()
n=input()
n=n.split()
for i in range(len(s)):
    if(s.count(s[i])==n.count(s[i])):
        c+=1
print(c)