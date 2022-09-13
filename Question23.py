class Disp:
    def getArray(self):
        a1=[]
        size = int(input("Enter limit of arrays\n"))
        print("Enter elements of array")
        for rows in range(size):
            row=[]
            for col in range(size):
                row.append(int(input()))
            a1.append(row)
        return a1,size

    def displayArray(self,arr1,s):
        print("Array elements are")
        for i in range(int(s)):
            print(arr1[i])
            
obj = Disp()
a1,size = obj.getArray()
obj.displayArray(a1,size)