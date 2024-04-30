n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    for j in range(i,n-1):
        print(' ',end=' ')
    for j in range(i+1,n):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print( )