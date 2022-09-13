limit=int(input("Enter a limit \n"))
sum=0
for i in range(1,limit+1):
    if (i%2)!=0:
        sum=sum+i
print("Sum of odd Numbers="+str(sum))