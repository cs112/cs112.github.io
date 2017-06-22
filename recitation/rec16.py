############################################################################
# Problems 
############################################################################
"""
SumOfOdds(L) (recursive) 
Without using iteration, write the recursive function sumOfOdds(L) that takes a 
list of integers and returns the sum of the odd numbers in that list.
"""

def sumOfOdds(L): 
    return 43 # implement your solution here! 

def testSumOfOdds():
    print("Testing sumOfOdds...", end="")
    assert(sumOfOdds([]) == 0)
    assert(sumOfOdds([1]) == 1)
    assert(sumOfOdds([2]) == 0)
    assert(sumOfOdds([1, 5, 7]) == 13)
    assert(sumOfOdds([2, 4, 5, 6, 2, 1]) == 6)
    assert(sumOfOdds([1, 1]) == 2)
    print("Passed!")

# testSumOfOdds() # uncomment to check your answer 

"""
minimum(L) (recursive)
Without using iteration, and without using the builtin min function or any other 
similar builtin function, write the recursive function minimum(L) that takes a 
list L of integers and returns the minimum value in the list.
"""
def minimum(L, index=0):
    return 42 # implement your solution here! 

def testMin():
    print("Testing min...", end="")
    assert(minimum([]) == None)
    assert(minimum([1]) == 1)
    assert(minimum([1, 1, 1]) == 1)
    assert(minimum([1, 6, 0, 7, 8]) == 0)
    assert(minimum([1, 2, 3, -5]) == -5)
    assert(minimum([-1, -4, -3]) == -4)
    print("Passed!")

# testMin() # uncomment to check your answer 

############################################################################
# Code Tracing  
############################################################################
def ct2(x, y, depth=0):
    print("  "*depth, "ct2(%d, %d)" %(x,y))
    if(x + y <= 5):
        result = x + y
    else:
        result = ct2(x-2, y-2, depth+1)
        result += 2*ct2(x//2, y/2, depth+1)
    print("  "*depth, "-->", result)
    return result

# print(ct2(3,4)) # uncomment to check your answer! 

############################################################################
# Bonus  
############################################################################
"""
hasConsecutiveDigits(n) (recursive) 
Without using iteration, write the recursive function hasConsecutiveDigits(n) 
that takes a possibly- negative int value n and returns True if that number 
contains two consecutive digits that are the same, and False otherwise.
"""
def hasConsecutiveDigits(n): 
    return 42 # implement your solution here! 

def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits...", end="")
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print("Passed")

# testHasConsecutiveDigits() # uncommment to check your answer! 

"""
minimum(L) without list slicing. 
If you solved minimum(L) without list slicing, think about how you would solve 
it with list slicing. If you solved it with list slicing, then think about how 
you would solve it without list slicing! 
Hint: to do it without list slicing, you may or may not need default parameter
"""
