a=input()
b=list(input().split())
c={}
for i in b:
    count=0
    for ele in a:
        if i==ele  :
            count+=1
    c[i]=count
print(c)
