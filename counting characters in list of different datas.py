a=list(input())
n=len(a)
count=0
print(a)
for i in a:
    if 64 < ord(i) > 91 or 94 < ord(i) > 123:
        print(i,end=' ')
        count+=1
print(count)