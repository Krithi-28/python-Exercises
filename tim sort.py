min_run=32
def calmin(n):
    r=0
    if n>=min_run:
        n>>1
    return n+r
def insertionsort(a,left,right):
    for i in range(left+1,right+1):
        key=i
        while key>left and a[key]<a[key-1]:
            a[key],a[key-1]=a[key-1],a[key]
            key-=1


def merge(a, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(a[l + i])
    for i in range(0, len2):
        right.append(a[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1

        else:
            a[k] = right[j]
            j += 1

        k += 1


    while i < len1:
        a[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        a[k] = right[j]
        k += 1
        j += 1
def timsort(a):
   n=len(a)
   minrun=calmin(n)
   for start in range(0,n,minrun):
       end=min(start+minrun-1,n-1)
       insertionsort(a,start,end)
   size = minrun
   while size < n:
       for left in range(0, n, 2 * size):
           mid = min(n - 1, left + size - 1)
           right = min((left + 2 * size - 1), (n - 1))
           if mid < right:
               merge(a, left, mid, right)

       size = 2 * size
a=list(map(int,input().split()))
timsort(a)
print(a)