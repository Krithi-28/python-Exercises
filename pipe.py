n=list(map(int,input().split()))
m=list(map(int,input().split()))
if sum(n)==sum(m):
    print("balanced")
elif sum(n)>sum(m):
    diff=sum(m)-sum(n)
    print(diff+2)
else:
    diff = sum(m) - sum(n)
    print(diff+2)