number = int(input("Enter any Number\n"))
flag=0
for i in range(2,number):
    if number%i==0:
        flag=1
        break
if flag==0:
    print("Entered Number is a Prime Number")
else:
    print("Entered Number is NOT a Prime Number")