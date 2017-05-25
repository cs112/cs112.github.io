################################################################################
# Challenge 1: largestDigit
# Find the largest digit in an integer
################################################################################

def largestDigit(n):
    return 42

def testLargestDigit():
    print("Testing largestDigit()...", end="")
    assert(largestDigit(1) == 1)
    assert(largestDigit(9233) == 9)
    assert(largestDigit(187932) == 9)
    assert(largestDigit(0) == 0)
    assert(largestDigit(10) == 1)
    assert(largestDigit(-1) == 1)
    assert(largestDigit(-236351) == 6)
    print("Passed!")