arr=[]
size=int(input("Enter size of array\n"))
print("Enter elements of List")
for i in range(size):
    arr.append(int(input()))
count=0
for i in range(size):
    if arr[i]%2==0:
        count=count+1
print("No of Even No's in the given List="+str(count))