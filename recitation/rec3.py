##############################################################################
# CT1 [7 mins] 
##############################################################################

k = 2
def t(k):
  print(k, end=" ")
  return k + 1
def y(s):
  global k
  print(k, end=" ")
  s = (s + 1) % 5
  k += s
  return t(s + k)
def g(s):
  return t(y(s) + y(k))
print(g(3), end=" ")
print(k)

##############################################################################
# CT2 [10 mins] 
##############################################################################

def f(x,y):
  for z in range(x,y):
    if (z%x == 0):
      print(z, end="")
    elif (z < (x+y)/2):
      print(".", end="")
    if (z%5 == 1):
      print("*", end="")
f(2, 16)

##############################################################################
# ROC [5 mins] 
##############################################################################

def rc1(n):
    if  (n  ==  0): return  False
    count = 0
    for x in  range(0,  100,  n):
        count +=  1
    # hint: here, x equals  the last  value in  the range
    return  ((count ==  5)  and (x//10  ==  x%10 +  4))

##############################################################################
# hasConsecutiveDigits [5 mins]
##############################################################################

def hasConsecutiveDigits(n):
  return 42 # replace with your solution

def testHasConsecutiveDigits():
  print("Testing hasConsecutiveDigits()...", end="")
  assert(hasConsecutiveDigits(0) == False)
  assert(hasConsecutiveDigits(123456789) == False)
  assert(hasConsecutiveDigits(1212) == False)
  assert(hasConsecutiveDigits(1212111212) == True)
  assert(hasConsecutiveDigits(33) == True)
  assert(hasConsecutiveDigits(-1212111212) == True)
  print("Passed!")

# testHasConsecutiveDigits()

##############################################################################
# nthPerfectNumber [10 mins]
##############################################################################

def nthPerfectNumber(n):
  return 42 # replace with your solution

def testNthPerfectNumber():
  print("Testing nthPerfectNumber()...", end="")
  assert(nthPerfectNumber(0) == 6)
  assert(nthPerfectNumber(1) == 28)
  # assert(nthPerfectNumber(2) == 496)  # this can be slow in Brython
  # assert(nthPerfectNumber(3) == 8128) # this can be slow even in Standard Python!
  print("Passed!")

# testNthPerfectNumber()

##############################################################################
# gcd [10 mins]
##############################################################################

def gcd(x, y):
  return 42 # replace with your solution

def testGcd():
  print("Testing gcd()...", end="")
  assert(gcd(3, 3) == 3)
  assert(gcd(3**6, 3**6) == 3**6)
  assert(gcd(3**6, 2**6) == 1)
  x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
  y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
  g =    7128 # 2**3 * 3**4 *               11**1
  assert(gcd(x, y) == g)
  print("Passed!")

# testGcd()

