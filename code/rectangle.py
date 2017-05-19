######################################################
# OOP Example:  Rectangle
######################################################

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return 2*(self.width + self.height)

    def doubleDimensions(self):
        self.width *= 2
        self.height *= 2
        
    def rotate90Degrees(self):
        (self.width, self.height) = (self.height, self.width)


r1 = Rectangle(10, 5)
r2 = Rectangle(3, 4)
print(r1.getArea())

# Non-OOP version of getArea

def getArea(r):
    return r.width * r.height

print(getArea(r2))
