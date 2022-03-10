def suma(n):
    s=str(n)
    s=list(s)
    c=0
    for i in range(len(s)):
        s[i]=int(s[i])
        c+=s[i]
    return c
n=int(input())
while(True):
    k=suma(n)
    if(k<10):
        print(k)
        break
    else:
        n=k