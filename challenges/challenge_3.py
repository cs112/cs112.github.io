################################################################################
# Challenge 3: longestDigitRun
#
# Write the function longestDigitRun(n) that takes a possibly-negative 
# int value n and returns the longest consecutive run of digits in an integer
################################################################################

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
