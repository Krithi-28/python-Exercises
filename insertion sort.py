a=list(map(int,input().split()))
n=len(a)
for j in range(n):
    for i in range(1,n):
        key=i
        if a[key]<a[i-1]:
            temp=a[key]
            a[key]=a[i-1]
            a[i-1]=temp
print(a)

