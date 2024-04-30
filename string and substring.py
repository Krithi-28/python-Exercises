a=input().split()
s1=input()
s2=input()
for i in range(len(a)-1):
    if a[i]==s1:
        for j in range(i+1,len(a)-1):
            if a[j] == s2:
                break
            print(a[j],end=' ')
sub1=list(s1)
sub2=list(s2)
for i in a:
    if i ==s1:
        x=a.index(i)
    if i == s2:
        y=a.index(i)
print(a[x+1:y])