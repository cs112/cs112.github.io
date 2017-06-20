###############################################################################
# Problem Solving: Heavyweight Line Class  
###############################################################################
'''
You have seen the TA do the Lightweight Line Class. Now let's improve it! 
Write the Line Class so that it passes testLineClass, and uses the OOP as 
appropriate.
'''

###############################################################################
# Pass these test cases! 
###############################################################################

def almostEqual(x, y):
    return (abs(x-y) < 10**-8)

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

    print('Passed.')

# testLineClass() # uncomment this line to add your solution