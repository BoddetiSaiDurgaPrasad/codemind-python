n=input()
s=n.split()
for i in range(len(s)):
    if(i%2==0):
        k=s[i]
        k=k[::-1]
        s[i]=k
x=" ".join(s)
print(x)