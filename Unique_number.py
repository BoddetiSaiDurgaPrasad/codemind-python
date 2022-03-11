n=int(input())
n=str(n)
k=list(n)
s=set(k)
s=list(s)

if(len(s)==len(k)):
    print("Unique Number")
else:
    print("Not Unique Number")