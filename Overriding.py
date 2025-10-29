class Shape:
    
    def __init__(self, height = 0, width = 0, length = 0, radius= 0):
        self.height = height
        self.width = width
        self.radius = radius
        self.length = length

    def area():
        pass

class circle(Shape):

    def __init__(self,radius):
       super().__init__(radius = radius)

    def area(self):
        ans = 3.14 * self.radius * self.radius
        print("Area of circle is: ", ans)


class Triangle(Shape):
      
      def __init__(self, height, length):
         super().__init__(height = height,length = length)
      def area(self):
       answ = 0.5 *  self.height* self.length
       print("The area of triangle is: ", answ)



class Rectangle(Shape):

    def __init__(self, width, length ):
       super().__init__(width = width, length = length)
    def area(self):
     ans2 = self.length * self.width

     print("The area of rectangle is: ", ans2)

class Square(Shape):
    def __init__(self, length):
       super().__init__(length = length)
    def area(self):
     ans1 = self.length * self.length
     print("The area of square is: ", ans1)


radius = float(input("Enter the radius: "))
length = float(input("Enter the lenght: "))
height = float(input("Enter the height: "))
width = float(input("Enter the width: "))

s = Shape(height, width, length, radius)

c = circle(radius)
c.area()

t = Triangle(height, length)
t.area()

r = Rectangle(width, length)
r.area()


s = Square(length)
s.area()





