n=int(input())
k=list(map(int,input().split()))
s=sum(k)
q=s//n
if(k.count(q)>=1):
    print("True")
else:
    print("False")