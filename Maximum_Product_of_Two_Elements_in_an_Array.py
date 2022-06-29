arr=list(map(int,input().split()))
m=v=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i!=j):
            m=(arr[i]-1)*(arr[j]-1)
            if(m>v):
                v=m
print(v)

