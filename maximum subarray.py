nums = list(map(int,input().split()))
sum=nums[0]
curr=nums[0]
for i in nums[1:]:
    curr=max(i,curr+i)
    sum=max(sum,curr)
print(sum)
