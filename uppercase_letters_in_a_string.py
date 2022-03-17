n=input()
c=0
for i in range(len(n)):
    if(n[i].isupper()==True):
        c+=1
print(c)