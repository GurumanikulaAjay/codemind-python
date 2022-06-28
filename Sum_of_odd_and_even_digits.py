n=int(input())
arr=list(map(int,input().split()))
s=v=diff=0
for i in range(n):
    if(i%2==0):
        s+=arr[i]
    else:
        v+=arr[i]
diff=v-s
if(diff==0):
    print("YES")
else:
    print("NO")
