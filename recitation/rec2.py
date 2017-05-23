###############################################
# 15-112 Summer 2017
# Recitation 2 Handout
###############################################

# Name:
# Andrew:
# Section:

# Please complete the following problem set and you TA will check you off. 
# There is nothing for you to turn in, but you will need to pass the test cases. 
# (please don't modify them except to add your own) If you have time, you may 
# also do the bonus.

# To test your functions, just uncomment the calls to the test functions

# For test functions. No need to touch this
def almostEqual(v1, v2):
    epsilon = 10**-4
    return abs(v1 - v2) < epsilon

###############################################
# Free Response (FR)
###############################################

'''
Write the function triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3) that
takes 6 int or float values that represent the three points (x1,y1), (x2,y2),
and (x3,y3), and returns as a float the area of the triangle formed by those
three points. Hint: you should make constructive use of the distance and
triangleArea functions we wrote in recitation yesterday
'''

def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):
    return 42

def testTriangleArea():
    print("Testing pittsburghHour()...", end="")
    assert(almostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16))
    assert(almostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250))
    assert(almostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),4*3**.5))
    assert(almostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,-2,2,5,5),0))
    print("Passed.")

# testTriangleArea() # uncomment this and run this file to test your function!

"""
Write the function eggCartons(eggs) that takes a non-negative integer number of 
eggs, and returns the smallest integer number of cartons required to hold that 
many eggs, where a carton may hold up to 12 eggs.
"""
def eggCartons(eggs):
    return 42 # replace with your solution

def testEggCartons():
    print("Testing eggCartons()...", end="")
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print("Passed.")

# testEggCartons() # uncomment this and run this file to test your function!

"""
Fabric must be purchased in whole yards. With this in mind, write the function 
fabricExcess(fabricInches) that takes a non-negative int or float representing 
the number of inches of fabric desired and returns as an int or float the number 
of inches of excess fabric that must be purchased (as purchases must be in whole 
yards, where a yard is 36 inches). Thus, since you need a whole yard when you 
buy 1 inch, fabricExcess(1) is 35. Similarly, fabricExcess(36) is 0, and 
fabricExcess(35.5) is 0.5.
"""
import math

def fabricExcess(fabricInches):
    return 42 # replace with your solution

def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1-d2) <= epsilon

def testFabricExcess():
    print("Testing fabricExcess()...", end="")
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    # use almostEqual when comparing floats
    assert(almostEqual(fabricExcess(35.5), 0.5))
    assert(almostEqual(fabricExcess(36.5), 35.5))
    print("Passed.")

# testFabricExcess() # uncomment this and run this file to test your function!

###############################################
# BONUS
###############################################

'''
Pool balls are arranged in rows where the first row contains 1 pool ball and
each row contains 1 more pool ball than the previous row. Thus, for example, 3
rows contain 6 total pool balls (1+2+3).

With this in mind, write the function numberOfPoolBalls(rows) that takes a
non-negative int value, the number of rows, and returns another int value, the
number of pool balls in that number of full rows.

For example, numberOfPoolBalls(3) returns 6. Also, note that the test function
is missing some test cases. Please write at least three yourself!
'''

def numberOfPoolBalls(rows):
    return 42

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(3) == 6)
    # put your test cases here
    print('Passed.')

# testNumberOfPoolBalls()

'''
This problem is the inverse of the previous problem. Write the function
numberOfPoolBallRows(balls) that takes a non-negative int number of pool
balls, and returns the smallest int number of rows required for the given
number of pool balls.

Thus, numberOfPoolBallRows(6) returns 3. Note that if ANY ball is in a row,
then you count that row, and so numberOfPoolBallRows(7) returns 4 (since the
4th row has a single ball in it).

NOTE: You may notice that this is a lot harder than the previous problem. Try
to come up with a mathematical formula on paper before coding anything. (This
is a helpful strategy for most, if not all programming challenges!)
'''

def numberOfPoolBallRows(balls):
    return 42

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assertEqual(numberOfPoolBallRows(0), 0)
    assertEqual(numberOfPoolBallRows(1), 1)
    assertEqual(numberOfPoolBallRows(2), 2)
    assertEqual(numberOfPoolBallRows(3), 2)
    assertEqual(numberOfPoolBallRows(4), 3)
    assertEqual(numberOfPoolBallRows(6), 3)
    assertEqual(numberOfPoolBallRows(7), 4)
    assertEqual(numberOfPoolBallRows(10), 4)
    assertEqual(numberOfPoolBallRows(11), 5)
    assertEqual(numberOfPoolBallRows(55), 10)
    assertEqual(numberOfPoolBallRows(56), 11)
    print('Passed.')

# testNumberOfPoolBallRows()
