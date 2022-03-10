n=int(input())
f=n*n
k=str(f)
k=list(k)
x=0
for i in range(len(k)):
    h=int(k[i])
    x+=h
if(x==n):
    print("Neon Number")
else:
    print("Not Neon Number")