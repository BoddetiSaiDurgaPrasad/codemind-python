n=int(input())
k=str(n)
k=list(k)
for i in range(len(k)):
    k[i]=int(k[i])
print(max(k))