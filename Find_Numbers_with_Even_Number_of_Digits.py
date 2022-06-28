






import math
n=int(input())
p=list(map(int,input().split()))
v=0
c=0
r=0
k=0
for i in range(n):
    v=p[i]
    c=0
    while p[i]>0 :
        r=p[i]%10
        c+=1
        p[i]=p[i]//10
    #print(c)
    if(c%2==0):
        k+=1
print(k)
        