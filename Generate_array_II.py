n=int(input())
a=list(map(int,input().split()))
c=0
i=0
while i<n-1:
    j=i
    while a[j+1]:
        print(a[j],end=" ")
        a[j+1]-=1
    i+=2