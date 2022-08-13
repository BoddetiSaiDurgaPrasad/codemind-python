def hexa(n):
    c=""
    for i in range(len(n)):
        if(n[i]=='0'):
            c+="0000"
        elif(n[i]=='1'):
            c+="0001"
        elif(n[i]=='2'):
            c+="0010"
        elif(n[i]=='3'):
            c+="0011"
        elif(n[i]=='4'):
            c+="0100"
        elif(n[i]=='5'):
            c+="0101"
        elif(n[i]=='6'):
            c+="0110"
        elif(n[i]=='7'):
            c+="0111"
        elif(n[i]=='8'):
            c+="1000"
        elif(n[i]=='9'):
            c+="1001"
        elif(n[i]=='A'):
            c+="1010"
        elif(n[i]=='B'):
            c+="1011"
        elif(n[i]=='C'):
            c+="1100"
        elif(n[i]=='D'):
            c+="1101"
        elif(n[i]=='E'):
            c+="1110"
        elif(n[i]=='F'):
            c+="1111"
    return c
    
k=int(input())
for i in range(k):
    n=input()
    print(hexa(n))