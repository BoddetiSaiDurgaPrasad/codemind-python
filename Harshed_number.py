n=int(input())
k=str(n)
k=list(k)
for i in range(len(k)):
    k[i]=int(k[i])
c=sum(k)
if(n%c==0):
    print("True")
else:
    print("False")