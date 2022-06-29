



import math
n=int(input())
c=0
for i in range(1,n) :
    if(pow(i,2)==n) :
        c=1;
        break;
if(c==1) :
    print(True)
else :
    print(False)
    
