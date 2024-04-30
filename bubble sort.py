a=list(map(int,input().split()))
n=len(a)
temp=0
count=0
for i in range(n):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            count+=1
print(count)
print(a)