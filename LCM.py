a,b=map(int,input().split())
j=1
if(a>b):
    a,b=b,a

while(True):
    if((b*j)%a==0):
        print(b*j)
        break
    j+=1
