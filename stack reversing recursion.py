def revstack(a,s,n):
    if s>=n//2:
        return
    a[s],a[n-s-1]=a[n-s-1],a[s]
    revstack(a,s+1,n)


n=int(input("enter no of datas:"))
a=[]
for i in range(n):
    data=int(input("enter data:"))
    a.append(data)
print(a)
s=0
n=len(a)
revstack(a,s,n)
print(a)
