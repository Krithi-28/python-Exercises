a=list(map(int,input().split()))
b={}
for ele in a:
    if ele in b:
        b[ele]+=1
    else:
        b[ele]=1
sorted_dict=dict(sorted(b.items(),key=lambda a:a[1],reverse=True))
for k in sorted_dict.keys():
    for i in range(sorted_dict[k]):
        print(k,end=' ')