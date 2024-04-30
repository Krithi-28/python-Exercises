n=int(input())
x=int(input())
fact=1
sum=1
for i in range(1,n):
    fact=fact*i
    sum+=(x**i)/fact
print(sum)