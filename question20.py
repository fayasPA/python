limit = int(input("Enter Limit"))
count=0
for i in range(1,limit+1):
    sCount=""
    for j in range(1,i+1):
        count = count + 1
        sCount = sCount + str(count) + " "
    print(sCount)