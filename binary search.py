def binarysearch (a, s, start, end):
    mid=(start+end) // 2
    if mid>=0 and mid<n:
        if s == a[mid]:
            return a[mid]
        elif s > a[mid]:
            start = mid + 1
            return binarysearch(a, s, start, end)
        else:
            end = mid - 1
            return binarysearch(a, s, start, end)
    else:
        return -1


b=list(map(int,input().split()))
s=int(input())
a=sorted(b)
n=len(a)
start=0
end=n
ind = binarysearch(a,s,start,end)
if ind ==-1:
    print("element not found")
else:
    print("element found at index",b.index(ind))
