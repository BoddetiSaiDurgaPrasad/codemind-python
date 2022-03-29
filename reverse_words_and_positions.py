c=input()
s=c.split()
s.reverse()
for i in range(len(s)):
    k=s[i]
    k=k[::-1]
    s[i]=k
x=" ".join(s)
print(x)