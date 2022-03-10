n=int(input())
k=n*n
s=str(n)
a=len(s)
ten=10**a
w=k%ten
if(w==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")