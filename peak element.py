a=list(map(int,input().split()))
n=len(a)
if n==1:
    print("peak element:",a[0])
else:
    if a[0]>a[1]:
        print("peak element:",a[0])
    if a[n-1]>a[n-2]:
         print("peak element:",a[n-1])

    for i in range(1,n-1,1):
        if a[i-1]<a[i] and a[i+1]<a[i]:
             print("peak element:",a[i])
