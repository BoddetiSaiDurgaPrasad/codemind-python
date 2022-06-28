c=int(input())
for i in range(c):
    ca=input()
    ca=int(ca,2)
    ca=oct(ca)
    ca=ca[2:]
    print(ca)