a=list(map(int,input().split()))
n=len(a)
rot=int(input("no of rotation:"))
for i in range(rot):
    last=a[n-1]
    for j in range(n-1,-1,-1):
        a[j]=a[j-1]
    a[0]=last
print(a)
