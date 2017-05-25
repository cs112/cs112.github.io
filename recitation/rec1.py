##############################################################################
# Code Tracing [10 mins] 
##############################################################################

def f(x): return (x**2)//(x%7)
def g(x): return x-1
def h(x, y): return (f(g(x)) % g(f(y)))
# print h(9, 13)

##############################################################################
# Programming Error [5 mins] 
##############################################################################

# What type(s) of errors does the following code produce? 
def example1(x): 
  return 1 + 2 // x 
f(0) 

def example2(x): 
  print x*x 

def cube(x):
  Return (x*3)


##############################################################################
# Problem Solving [15 mins] 
##############################################################################

def distance(x1, y1, x2, y2):
  return 42

# Use Heron's Formula to calculate the area of triangle with sides a, b, c
def triangleArea(s1, s2, s3):
  return 42

def isFactor(f, n): 
  return 42

##############################################################################
# Test Functions
##############################################################################
def almostEqual(d1, d2):
  epsilon = 10**-8
  return (abs(d2 - d1) < epsilon)

def testTriangleArea():
  print('Testing triangleArea()... ', end='')
  assert(almostEqual(triangleArea(3,4,5), 6))
  assert(almostEqual(triangleArea(1,2,2.8), (2.9 * 1.9 * 0.9 * 0.1)**0.5))
  print('Passed.')

def testTriangleAreaByCoordinates():
  print('Testing triangleAreaByCoordinates()... ', end='')
  assert(almostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16))
  assert(almostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250))
  assert(almostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),4*3**.5))
  assert(almostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39))
  assert(almostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20))
  print('Passed.')

def testIsFactor():
  print('Testing isFactor()... ', end='')
  assert(isFactor(1,1) == True)
  assert(isFactor(2,10) == True)
  assert(isFactor(-5,25) == True)
  assert(isFactor(5,0) == True)
  assert(isFactor(0,0) == True)
  assert(isFactor(2,11) == False)
  assert(isFactor(10,2) == False)
  assert(isFactor(0,5) == False)
  print('Passed.')

def testAll():
    testTriangleArea()
    testTriangleAreaByCoordinates()
    testIsFactor()

if __name__ == '__main__':
    testAll()
