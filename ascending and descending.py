a=list(map(int,input().split()))
n=len(a)
mid=int(n/2)
temp=0
for i in range(mid-1):
    if a[i]>a[i+1]:
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
for i in range(mid,n-1):
    if a[i]<a[i+1]:
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
print(a)