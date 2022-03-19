a=input()
b=input()
a=a.lower()
b=b.lower()
#print(a,b)
a=a.split()
b=b.split()
c=0
for i in range(len(a)):
    if(b.count(a[i])>=1):
        c+=1
print(c)