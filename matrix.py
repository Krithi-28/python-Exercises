matrix=[]
row=int(input("enter no of rows:"))
col=int(input("enter no of cols:"))
for i in range(row):
    a=[]
    for j in range(col):
        b=int(input("enter number:"))
        a.append(b)
    matrix.append(a)
print(matrix)