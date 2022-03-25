n=(input())
n=n.lower()
s=n.split()
count=0
for i in range(len(s)):
    c=s[i]
    c=c[::-1]
    if(c==s[i]):
        count+=1
print(count)