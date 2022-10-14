n=int(input())
m=int(input())
for i in range(n,m+1):
    temp=i
    c=0
    k=0
    while(i>0):# 21
        c=c+1 
        r=i%10
        if(r==0):
            break
        elif(temp%r==0):
            k=k+1 
        i=i//10
    if(c==k):
        print(temp,end=" ")
    
    
        
        
            