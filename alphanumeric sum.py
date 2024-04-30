a=input()
count=0
for i in a:
    if ord(i)>=48 and ord(i)<=57:
        count+=int(i)
print(count)