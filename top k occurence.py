nums=list(map(int,input().split()))
k=int(input())
d={}
a=[]
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for key,values in d.items():
    if d[key]>=k:
        a.append(key)
print(a)
