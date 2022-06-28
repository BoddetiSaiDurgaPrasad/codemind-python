c=int(input())
while(c):
    k=(input())
    k=int(k,8)
    k=bin(k)
    k=k[2:]
    print((k))
    c-=1