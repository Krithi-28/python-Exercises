a=list(map(int,input().split()))
n=len(a)
k=int(input())
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]+a[j]==k:
            count+=1
print(count)
