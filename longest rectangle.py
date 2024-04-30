h=[2,4]
a=[]
i=0
while i<len(h):
    if h[i+1]>=h[i]:
        sum=h[i]+h[i]
        a.append(sum)
    i+=2
print(max(a))
# heights = [2,1,5,6,2,3]


