n,m=map(int,input().split())
while(True):
    if(n>m):
        k=n%m
        if(k==0):
            print(m)
            break
        else:
            n=m
            m=k
    else:
        n,m=m,n