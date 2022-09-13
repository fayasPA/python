limit=int(input("Enter any limit \t"))
for i in range(1,limit+1):
    star=""
    for j in range(i):
        star=star+str(j+1)+" "
    print(star)
