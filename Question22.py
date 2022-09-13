def getArray():
    a1=[]
    a2=[]
    size = int(input("Enter limit of arrays\n"))
    print("Enter elements of 1st array")
    for rows in range(size):
        row=[]
        for col in range(size):
            row.append(int(input()))
        a1.append(row)
    print("Enter elements of 2nd array")
    for rows in range(size):
        row=[]
        for col in range(size):
            row.append(int(input()))
        a2.append(row)
    return a1,a2,size

def addArray(arr1,arr2,s):
    arrSum=[]
    for i in range(int(s)):
        row=[]
        for j in range(int((s))):
            row.append(arr1[i][j] + arr2[i][j])
        arrSum.append(row)
    return arrSum

def displayArray(result,s):
    print("Sum of Array 1 and Array 2 is")
    for i in range(int(s)):
        print(result[i])

a1,a2,size = getArray()
res = addArray(a1,a2,size)
displayArray(res,size)
