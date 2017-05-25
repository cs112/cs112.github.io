################################################################################
# Challenge 2: 
#
# Palindromic number: a number that is both palindromic and prime. 
# A palindromic number is a number that remains the same when its digits are 
# reversed
################################################################################
def nthPalindromicPrime(n):
    return 42


def testNthPalindromicPrime():
    print("Testing nthPalindromicPrime()...", end="")
    assert(nthPalindromicPrime(0) == 0)
    assert(nthPalindromicPrime(1) == 1)
    assert(nthPalindromicPrime(2) == 2)
    assert(nthPalindromicPrime(12) == 33)
    assert(nthPalindromicPrime(20) == 111)
    assert(nthPalindromicPrime(21) == 121)
    print("Passed!")
