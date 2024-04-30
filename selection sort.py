a=list(map(int,input().split()))
n=len(a)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    a[i],a[min]=a[min],a[i]
print(a)