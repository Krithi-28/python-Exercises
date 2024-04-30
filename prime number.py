import math
a= list(map(int,input().split()))
count=0
sum=0
for ele in a:
    if ele==1:
        continue
    sq=int(math.sqrt(ele))
    if sq<2:
        for j in range(2,ele):
            if ele % j!=0:
                count+=1
                sum+=ele
    for i in range(2,sq+1):
        if ele % i!=0:
            count+=1
            sum+=ele
print(count)
print(sum)