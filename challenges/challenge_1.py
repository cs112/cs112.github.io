################################################################################
# Challenge 1: largestDigit
# Find the largest digit in an integer
################################################################################

def largestDigit(n):
    n = abs(n)
    answer = 0
    check =0
    while n >0:
        check = n%10
        n //= 10
        if check > answer:
            answer = check
    return answer

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