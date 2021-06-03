class Shape(object):
    def __init__(self,width,heigh):
        self.width=width
        self.heigh=heigh
        
    def Area(self):
         return self.width*self.heigh
    
    def __str__(self):
        return "[ 너비 : "+str(self.width)+" ]"
    
    def __lt__(self,other):
        return self.Area()<other.Area()

class Rectangle(Shape):
    def Circum(self):
        return (self.width+self.heigh)*2
    
    def __str__(self):
        return "[ 넓이 : "+str(self.width*self.heigh*1/2)+" ]"
    
def Square(Shape):
    def __init__(self,width):
        self.width=width
    
    def Circum(self):
        return self.width*4
    
    def Area(self):
        return self.width**2
    
    def __str__(self):
        return "[ 한 변의 길이 : ",+str(self.width)+" ]"
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def Circum(self):
        return 3.14*2*self.radius
    
    def Area(self):
        return 3.14*(self.radius)**2
    
    def __str__(self):
        return "[ 지름 : "+str(self.Circum())+" ]"
    
    def __lt__(self,other):
        return self.Area()<other.Area()

r1=Rectangle(2,3)
print(r1)
r2=Rectangle(4,5)
print(r2.Circum())
print(r2)
s=Square(5) 
print(s.Circum()) 
print(s.Area()) 
print(s) 
c=Circle(10)
print(c) 
print(c.Area()) 
print(r1<r2)