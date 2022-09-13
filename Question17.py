class MathOp:

    def inpa(self):
        num1 = (input("Enter two numbers\n"))
        num2 = (input())
        return num1,num2

        
    def addition(self):
        numb1,numb2 = obj.inpa(self)
        res=int(numb1) + int(numb2)
        print("Sum ="+str(res))
    def subtraction(self):
        numb1,numb2 = MathOp.inpa(self)
        res=int(numb1) - int(numb2)
        print("Subtraction ="+str(res))
    def multiplication(self):
        numb1,numb2 = MathOp.inpa(self)
        res=int(numb1) * int(numb2)
        print("Multiplication ="+str(res))
    def division(self):
        numb1,numb2 = MathOp.inpa(self)
        res=int(numb1) / int(numb2)
        print("Division ="+str(res))
obj = MathOp()
choice = int(input("Select any of the following\n1.ADDITION\t2.SUBTRACTION\n3.MULTIPLICATION\t4.DIVISION\n"))
if choice==1:
    obj.addition()
elif choice==2:
    obj.subtraction()
elif choice==3:
    obj.multiplication()
elif choice==4:
    obj.division()
else:
    print("INVALID CHOICE")


