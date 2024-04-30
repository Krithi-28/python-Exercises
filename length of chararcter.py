a=input().split()
n=len(a)
leng=0
for i in range(n):
    leng+=len(a[i])
print(leng)