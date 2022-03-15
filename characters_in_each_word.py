n=input()
s=n.split()
for i in range(len(s)):
    c=s[i]
    x=len(c)
    s[i]=x
print(*s)