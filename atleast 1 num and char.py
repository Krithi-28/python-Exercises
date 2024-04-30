a=input()
n=len(a)
count=0
for i in a:
    if 47 < ord(i) > 58:
        print(i,end=' ')
        count+=1
    if 64 < ord(i) > 91 or 94 < ord(i) > 123:
        print(i,end=' ')
        count+=1
if count >= 2:
    print("True")
else:
    print("False")