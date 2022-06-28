


n=int(input())
arr=list(map(int,input().split()))
x=int(input())
ma=0
for i in range(n):
    if(arr[i]>ma):
        ma=arr[i]
for i in range(n):
    if(arr[i]+x>=ma):
        print(True,end=" ")
    else:
        print(False,end=" ")

