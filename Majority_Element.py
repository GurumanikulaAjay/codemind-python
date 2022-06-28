



n=int(input())
p=list(map(int,input().split()))
k=0
v=0
c=0
for i in range(n):
    c=0
    k=p[i]
    for j in range(n):
        if(k==p[j]):
            c+=1
    if(c>n//2):
        print(p[i])
        break;
        
