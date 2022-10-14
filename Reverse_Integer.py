def sum(a):
    if(a>0):
        c=a
        d=0
        while(c!=0):
            d=d*10+c%10
            c=c//10
        print(d)
    else:
        c=-a
        d=0
        while(c!=0):
            d=d*10+c%10
            c=c//10
        print(-d)
        
         
n=int(input())
sum(n)