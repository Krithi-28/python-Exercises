a=input()
count=0
for i in a:
    if i=='1' or i=='0':
        count+=1
if count== len(a):
    print("yes")
else:
    print("no")
c=set(a)
b={'0','1'}
if c==b or c=={'0'} or c=={'1'}:
    print("yes")
else:
    print("no")