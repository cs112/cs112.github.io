##############################################################################
# Loop CT [5 mins] 
##############################################################################
def ct2(n):
    k = 0
    total = 0
    while (n >= k):
        print('k =', k)
        for i in range(k):
            total += n%10
            n //= 10
            print(i, n%10, total)
        k += 1
    print('total =', total)

# print(ct2(1234)) # uncomment this line to check your answer! 

##############################################################################
# ROC [5 mins] 
##############################################################################

def rc1(n):
  if ((n < 0) or (n > 99)): return False
  d1 = n%10
  d2 = n//10
  m = 10*d1 + d2
  return ((m < n) and (n < 12))

n = 42 # replace 42 with your answer
# print(rc1(n)) # uncomment this line to check your answer!


##############################################################################
# FR [30 mins] 
##############################################################################

"""
longestDigitRun(n)
Write the function longestDigitRun(n) that takes a positive int value n 
and returns the length of the longest consecutive run. For example, 
longestDigitRun(117773732) returns 3 (because the longest consecutive run 
is a run of 3 consecutive 7's), and longestDigitRun(677886) returns 2 (because 
the longest consecutive run(s) is a run of 2 consecutive 7's or 8's). 

Hint: Loop through the digits of n, starting at the one's. You would want to keep 
track of the following variables: previous digit, current digit, count of best 
consecutive run, count of current consecutive run
"""
def longestDigitRun(n): 
  return 42

def testLongestDigitRun():
    print("Testing longestDigitRun()...", end="")
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(22233) == 3)
    assert(longestDigitRun(1122444) == 3)
    assert(longestDigitRun(1234) == 1)
    assert(longestDigitRun(11111555) == 5)
    assert(longestDigitRun(122234) == 3)
    print("Passed!")

# testLongestDigitRun() # uncomment this line to test your function

"""
isSubnumber(m, n)
Write the function isSubnumber(m, n) that takes positive ints m, n and returns 
True if m is a subnumber of n, and False otherwise. m is subnumber of n if n 
contains m. So isSubnumber(23, 1234) returns True because 1234 contains 23, and 
isSubnumber(679, 79) and isSubnumber(35, 34575) returns False.   

Hint: Write a helper function that checks if there is a subnumber m at given 
location i in integer n. 
"""
def isSubnumber(m, n):
  return 42

def testIsSubnumber():
    print("Testing isSubnumber()...", end="")
    assert(isSubnumber(1, 1) == True)
    assert(isSubnumber(23, 1234) == True)
    assert(isSubnumber(29, 1229) == True)
    assert(isSubnumber(35, 34575) == False)
    assert(isSubnumber(679, 79) == False)
    assert(isSubnumber(2, 152287) == True)
    print("Passed!")

# testIsSubnumber() # uncomment this line to test your function

##############################################################################
# Bonus  
##############################################################################

"""
nthIsolatedPrime(n)
An isolated prime (also known as single prime or non-twin prime) is a prime 
number p such that neither p − 2 nor p + 2 is prime. In other words, p is not 
part of a twin prime pair. For example, 23 is an isolated prime, since 21 and 
25 are both composite.
Write the function nthIsolatedPrime(n) that returns the nth isolated prime. So 
nthIsolatedPrime(0) returns 2, and nthIsolatedPrime(1) returns 23
"""
def nthIsolatedPrime(n): 
  return 42

def testIsolatedPrime():
    print("Testing isIsolatedPrime()...", end="")
    assert(nthIsolatedPrime(0) == 2)
    assert(nthIsolatedPrime(1) == 23)
    assert(nthIsolatedPrime(2) == 37)
    assert(nthIsolatedPrime(3) == 47)
    assert(nthIsolatedPrime(4) == 53)
    assert(nthIsolatedPrime(5) == 67)
    print("Passed!")

# testIsolatedPrime() # uncomment this line to test your function

