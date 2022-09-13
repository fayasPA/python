arr = []
size=int(input("Enter the size of array\n"))
print("Enter values of array")
for i in range(size):
    arr.append(int(input()))
print("Sorted Array")
for i in range(size):
    for j in range(i,size):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
Sarr=""
for i in range(size):
    Sarr=Sarr + str(arr[i]) + " "
print(Sarr)