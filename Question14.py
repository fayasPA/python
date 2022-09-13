from numpy import *
size = int(input("Enter Limit of 2 arrays\n"))
arr3=[]
arr1=[]
arr2=[]
print("Enter Elements of 1st array")
for row in range(size):
    rows=[]    
    for column in range(size):
        rows.append(int(input()))           # accepting each row element of matrix
    arr1.append(rows)                       # Adding row into the matrix

print("Enter Elements of 2nd array")
for row in range(size):
    rows=[]
    for column in range(size):
        rows.append(int(input()))
    arr2.append(rows)

print("Sum of two arrays are\n")
for row in range(size):
    rows=[]
    for col in range(size):
        rows.append(arr1[row][col] + arr2[row][col])
    arr3.append(rows)

m=matrix(arr3)
print(m)