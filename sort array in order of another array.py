a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(b)):
    for j in range(len(a)):
        if a[j]==b[i]:
            c.append(a[j])
for i in a:
    if i not in c:
        d.append(i)
print(c+sorted(d))
#2 1 2 5 7 1 9 3 6 8 8
#2 1 3 8