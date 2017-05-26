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
    assert(nthPalindromicPrime(0) == 2)
    assert(nthPalindromicPrime(1) == 3)
    assert(nthPalindromicPrime(2) == 5)
    assert(nthPalindromicPrime(12) == 373)
    assert(nthPalindromicPrime(13) == 383)
    print("Passed!")

testNthPalindromicPrime()

