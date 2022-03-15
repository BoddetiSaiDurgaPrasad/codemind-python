n=input()
s=n.split()
for i in range(len(s)):
    c=s[i]
    c=c[::-1]
    s[i]=c
a=" ".join(s)
print(a)