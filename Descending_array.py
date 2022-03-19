n=int(input())
s=list(map(int,input().split()))
a=s.copy()
a.sort()
a.reverse()
#print(a)
for i in range(n):
    if(a[i]!=s[i]):
        print("no")
        break
else:
    print('yes')