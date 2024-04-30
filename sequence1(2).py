n=int(input())
x=0
y=0
for i in range(1,n+1):
    if i%2!=0:
        print(x,end=' ')
        x=x+7
    else:
        print(y,end=' ')
        y=y+6
