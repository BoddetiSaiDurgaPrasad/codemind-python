n=int(input())
k=list(map(int,input().split()))
a,b=map(int,input().split())
c=sum(k)
h=0
for i in range(len(k)):
    if(k[i]<a or k[i]>b):
        h+=k[i]
print(h)