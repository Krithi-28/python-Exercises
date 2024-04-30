a=list(map(int,input().split()))
n= len(a)
profit=0
for i in range(1,n):
    if a[i]>a[i-1]:
        profit+=a[i]-a[i-1]
print(profit)