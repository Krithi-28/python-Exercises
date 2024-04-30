a=list(map(int,input().split()))
b=a
for i in range(len(b)-1):
    if abs(b[i]-b[i+1])==1:
        b[i],b[i+1]=b[i+1],b[i]
        print(b)
if sorted(a)==b:
    print("yes")
else:
    print("No")
#1 0 3 2