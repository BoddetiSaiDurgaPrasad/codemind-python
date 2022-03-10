from math import sqrt
n=int(input())
k=int(sqrt(n))
for i in range(k):
    if(k*(k+1)==n):
        print("YES")
        break
else:
    print("NO")