



a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n=set(arr)
m=set(arr2)
n=list(arr)
m=list(arr2)
x=0
for i in range(a):
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j]:
                 if arr[i]!=-1000:
                     arr[j]=-1000
for i in range(b):
    for j in range(b):
        if i!=j:
            if arr2[i]==arr2[j]:
                if arr2[i]!=-100:
                    arr2[j]=-100
for i in arr:
    if i!=-1000:
        if i  not in arr2:
            print(i,end=" ")
for i in arr2:
    if i!=-100:
        if i not in arr:
           print(i,end=" ")
#print(x)