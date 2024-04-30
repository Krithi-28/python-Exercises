a=input()
n=len(a)
mid=n//2
for i in range(mid):
    flag=1
    if a[i]==a[mid+1]:
        flag=0
        mid=mid+1
    else:
        flag=1
if flag==0:
    print("symmetric")
else:
    print("not a symmetric")
for i in range(n//2):
    count=1
    if a[i]==a[n-1]:
        count=0
        n-=1
    else:
        count=1
        n=-1
if count==0:
    print("palindrome")
else:
    print("not a palindrome")