a=list(map(int,input().split()))
n=len(a)
tot=(n+1)*(n+2)/2
asum=sum(a)
ans=tot-asum
print(int(ans))