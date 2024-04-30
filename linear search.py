a=list(map(int,input().split()))
s=int(input())
c=-1
for i in  a:
    if i==s:
        c=a.index(i)
        break
if c==-1:
    print("element not found")
else:
    print("element is found at index",c)