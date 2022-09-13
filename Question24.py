class Area:
    def circle(self,radius):
        print("Area circle")
        area = 3.14*radius*radius
        print("Area of circle= "+str(area))
    def square(length):
        area = length*length
        print("Area of square= "+str(area))
    
    def rectangle(length,width):
        area = length*width
        print("Area of rectangle= "+str(area))
    
    def triangle(base,height):
        area = 0.5*base*height
        print("Area of triangle= "+str(area))



class MyClass(Area):
    def circle(self):
        r = float(input("Enter radius of circle\n"))
        Area.circle(self,r)

    def square(self):
        l = float(input("Enter length of square\n"))
        Area.square(l)
    
    def rectangle(self):
        l = float(input("Enter length and width of rectangle\n"))
        w = float(input())
        Area.rectangle(l,w)
    
    def triangle(self):
        b = float(input("Enter base and height of triangle\n"))
        h = float(input())
        Area.triangle(b,h)


mc = MyClass()
# mc.circle()
choice = int(input("Enter your choice\n1.CIRCLE\n2.SQUARE\n3.RECTANGLE\n4.TRIANGLE\n"))
if choice==1:
    mc.circle()
elif choice == 2:
    mc.square()
elif choice == 3:
    mc.rectangle()
elif choice == 4:
    mc.triangle()
else:
    print("INVALID CHOICE")

