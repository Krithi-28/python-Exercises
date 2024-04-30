m=list(map(int,input().split()))
n=list(map(int,input().split()))
u=m+n
length=len(u)
for i in range(len(u)-1):
    for j in range(i+1,len(u)):
        if u[i]==u[j]:
            length=length-1
print("union count:",length)
count=0
for i in range(len(m)):
    for j in range(len(n)):
        if m[i]==n[j]:
            count+=1
print("intersection count:",count)