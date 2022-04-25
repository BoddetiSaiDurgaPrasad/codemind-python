n=int(input())
k=list(map(int,input().split()))
c=k.count(0)
z=k.count(1)
if(c+z==n):
    print("True")
else:
    print("False")