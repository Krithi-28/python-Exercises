a=input()
if len(a)< 3:
    print(a)
else:
    if a[len(a)-3:]=='ing':
        print(a+'ly')
    else:
        print(a+'ing')