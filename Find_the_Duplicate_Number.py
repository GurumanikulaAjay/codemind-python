

t=int(input())
p=list(map(int,input().split()))
c=0
for j in range(t):
    for k in range(t):
        if(j!=k):
            if(p[j]==p[k]):
                print(p[j])
                c=1
                break
    if(c==1):
        break
            