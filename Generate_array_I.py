

n=int(input())
a=list(map(int,input().split()))
for i in range(0,n-1,2):
    j=i
    while a[j+1]:
        print(a[j],end=" ")
        a[j+1]-=1
