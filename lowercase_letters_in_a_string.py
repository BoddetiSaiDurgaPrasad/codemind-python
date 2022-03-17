n=input()
c=0
for i in range(len(n)):
    if(n[i].islower()==True):
        c+=1
print(c)