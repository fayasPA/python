arr1=[]
arr2=[]
size=int(input("Enter size of arrays \n"))
print("Enter elements of 1st array")
for i in range(size):
    arr1.append(int(input()))
print("Enter elements of 2nd array")
for i in range(size):
    arr2.append(int(input()))
for i in range(size):
    temp=arr1[i]
    arr1[i] = arr2[i]
    arr2[i]=temp
Sarr1=""
Sarr2=""
print("Arrays after swapping:")
for i in range(size):
    Sarr1=Sarr1+str(arr1[i])+" "
    Sarr2=Sarr2+str(arr2[i])+" "
print("1st Array:"+Sarr1+"\n2nd Array:"+Sarr2)