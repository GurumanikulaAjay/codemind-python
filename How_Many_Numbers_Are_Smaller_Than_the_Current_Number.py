


import math
n=int(input())
p=list(map(int,input().split()))
v=0
c=0
r=0
k=0
b=[]
for i in range(n):
    c=0
    for j in range(n):
        if(i!=j):
            if(p[j]<p[i]):
                c+=1
    b.append(c)
for i in range(n):
    print(b[i],end=" ")