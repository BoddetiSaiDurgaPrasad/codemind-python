n=int(input())
k=str(n)
k=list(k)
h=1
c=0
for i in range(len(k)):
    hq=int(k[i])
    c+=hq
    h*=hq
if(h==c):
    print("Spy Number")
else:
    print("Not Spy Number")