n=input()
#print(n)
#n=n.lower()
s=n.split()
c=s[-1]
if(min(c).isupper()==True):
    h=min(c)
    h=h.lower()
    if(c.count(h)>=1):
        print(h)
    else:
        print(min(c))
else:
    print(min(c))