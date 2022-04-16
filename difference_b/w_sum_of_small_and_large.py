n=input()
c=n.split()
s1,s2=0,0
for i in range(len(c)):
    k=c[i]
    k1=ord(min(k))
    k2=ord(max(k))
    s1+=k1
    s2+=k2
print(abs(s1-s2))