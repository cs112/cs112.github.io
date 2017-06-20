"""
Part 1: Ultra Heavyweight Line Class 
You have seen Lightweight and Heavyweight Line Class yesterday. Now let's make 
it Ultra Heavyweight by adding the hash function to pass these test cases! 
"""

class Line(object):

    def __init__(self, slope, yIntercept):
        self.slope = slope
        self.yIntercept = yIntercept

    def __str__(self):
        if (self.slope != 0 and abs(self.slope) != 1) and self.yIntercept > 0:
            return ("y=%dx+%d" % (self.slope, self.yIntercept))
        elif self.slope == 0:
            return ("y=%d" % (self.yIntercept))
        elif self.slope == 1: 
            return ("y=x+%d" % (self.yIntercept))
        elif self.slope == -1:
            return ("y=-x+%d" % (self.yIntercept))
        elif self.yIntercept < 0:
            return ("y=%dx-%d" % (self.slope, -self.yIntercept))

    def getSlope(self):
        return self.slope

    def getIntercept(self):
        return self.yIntercept

    def getIntersection(self, line2):
        if self.isParallelTo(line2): return None
        x = (line2.getIntercept() - 
            self.getIntercept())/(self.getSlope() - line2.getSlope())
        y = self.getSlope()*x + self.getIntercept()
        return (x,y)

    def isParallelTo(self, line2):
        return self.getSlope() == line2.getSlope()

    def getHorizontalLine(self, x):
        y = self.getSlope()*x + self.getIntercept()
        return Line(0, y)

    def __eq__(self, line2):
        return (isinstance(line2, Line) and self.getSlope() == line2.getSlope() 
            and self.getIntercept() == line2.getIntercept())

    # implement your __hash__ function! 

def almostEqual(x, y): return abs(x-y) < 10**(-8)

def testLineClass():
    print('Testing Line class...', end='')
    assert(str(Line(2,5))  == "y=2x+5")
    assert(str(Line(2,-5)) == "y=2x-5")
    assert(str(Line(0,5))  == "y=5")
    assert(str(Line(1,5))  == "y=x+5")
    assert(str(Line(-1,5)) == "y=-x+5")
    assert(str(Line(0,-5)) == "y=-5")
    assert(str(Line(0,0))  == "y=0")

    line1 = Line(2,3)
    assert(str(line1) == "y=2x+3")
    assert(line1.getSlope() == 2)
    assert(type(line1.getSlope()) == int)
    assert(line1.getIntercept() == 3)
    line2 = Line(6,-5)
    assert(str(line2) == "y=6x-5")
    assert(line2.getSlope() == 6)
    assert(line2.getIntercept() == -5)

    (x,y) = line1.getIntersection(line2) # (2, 7)
    assert(almostEqual(x, 2) and almostEqual(y, 7))

    line3 = Line(2, -3)
    (x,y) = line3.getIntersection(line2) # (0.5, -2)
    assert(almostEqual(x, 0.5) and almostEqual(y, -2))

    # parallel lines do not intersect
    assert(Line(2,3).getIntersection(Line(2,4)) == None)

    assert(line3.isParallelTo(line1) == True)
    assert(line3.isParallelTo(line2) == False)

    # getHorizontalLine returns a line that is horizontal
    # to the given line, intersecting at the given x value.
    line4 = line3.getHorizontalLine(4)
    assert(str(line4) == "y=5")
    assert(line4.getSlope() == 0)
    assert(line4.getIntercept() == 5)
    
    assert(Line(1, 2) == Line(1, 2))
    assert(Line(1, 2) != Line(1, 3))
    assert(not (Line(1, 2) == "don't crash here!"))

    s = set()
    assert(Line(1, 2) not in s)
    s.add(Line(1, 2))
    assert(Line(1, 2) in s)
    s.remove(Line(1, 2))
    assert(Line(1, 2) not in s)

    print('Passed!')

testLineClass()

"""
Part 2: Queue and Priority Queue
Queue and Priority Queue are useful "First-In-First-Out" data structures in 
Computer Science. You don't need to know what they are to do this exercise, but 
if you are interested, here is a description 
http://www.geeksforgeeks.org/queue-data-structure/

Write the Q (for Queue) and PQ (for Priority Queue) classes that pass the 
following test case! Use inheritence when appropriate.

"""

def testQueue(): 
    print("Test Q and PQ...", end="")
    assert(Q.numQs == 0)
    q = Q()
    assert(str(q) == "<Q of size 0>")
    q.add(5)
    q.add(3)
    assert(str(q) == "<Q of size 2>")
    assert(q.remove() == 5) # first-in, first-out!
    assert(str(q) == "<Q of size 1>")
    assert(q.remove() == 3)
    assert(str(q) == "<Q of size 0>")
    assert(Q.numQs == 1)

    q1 = Q()
    q1.add(42)
    q2 = Q()
    q2.add(42)
    q3 = Q()
    q3.add(99)
    assert(q1 == q2)
    assert(q1 != q3)
    assert(Q.numQs == 4)

    pq = PQ()
    assert(type(pq) == PQ)
    assert(isinstance(pq, Q))

    pq.add(4)
    pq.add(1)
    pq.add(2)
    pq.add(3)
    assert(str(pq) == "<PQ of size 4>")
    assert(pq.remove() == 1)
    assert(pq.remove() == 2)
    assert(str(pq) == "<PQ of size 2>")

    print("Passed!")

testQueue()