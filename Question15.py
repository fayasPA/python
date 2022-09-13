from array import *
def main():
    arr1=array('i',[])
    arr1=getArray()
    displayArray(arr1)

def getArray():
    arr=array('i',[])
    limit=int(input("Enter limit of array\n"))
    print("Enter elements of array")
    for i in range(limit):
        arr.append(int(input()))
    return arr

def displayArray(arr1):
    print("Array values are:")
    values = ""
    for i in arr1:
        values = values + str(i) + " "
    print(values)

main()


