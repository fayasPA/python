from array import *
arr=array('i',[])
new_arr=array('i',[])
limit = int(input("Enter size of array\n"))
print("Enter elements of array")
for i in range(limit):
    arr.append(int(input()))

print("OUTPUT:")
for i in range(limit-1):
    new_arr.append(arr[i]*arr[i+1])
line=""
for i in new_arr:
    line = line + str(i) + " "
print(line)