
############################################################################
# Solve this problem 
############################################################################
"""
mostCommonName
Write the function mostCommonName, that takes a list of names (such as 
["Jane", "Aaron", "Cindy", "Aaron"], and returns the most common name in this 
list (in this case, "Aaron"). If there is more than one such name, return a 
list of the most common names, in alphabetical order (actually, in whatever 
order sorted() uses). 
So mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) returns the list 
["Aaron", "Jane"]. If the list is empty, return None.  Also, treat names case 
sensitively, so "Jane" and "JANE" are different names.
No sets or dictionaries! 
"""
def mostCommonName(names): 
    return 42 # write your solution here! 

def testMostCommonName():
    print("Testing Most Common Name...", end="")
    assert(mostCommonName(["Roman", "Corey", "Aditri", "Corey"]) == "Corey")
    assert(sorted(mostCommonName(["Rishabh", "Blair", "Xinhui", "Blair", 
                                            "Xinhui"])) == ["Blair", "Xinhui"])
    assert(mostCommonName(["Kyle"]) == "Kyle")
    assert(sorted(mostCommonName(["Nikolai", "Andrew", "Nanaki"])) == 
                                            ["Andrew", "Nanaki", "Nikolai"])
    assert(mostCommonName([]) == None)
    print("Passed!")

# testMostCommonName() # uncomment to test your function! 

############################################################################
# Recitation Materials For Your Studying Pleasure 
############################################################################

# 2D List Code Tracing 
import copy

a = [[1],[2]]
(b,c,d) = (a, copy.copy(a), copy.deepcopy(a))
e = a[0][0]
a[0][0] += 1
print("e", e)
print("a", a)
b[0][0] += 2
c[1][0] += 3
d[1][0] += 4
a[0] = c[0]
b[0] = d[0]
for L in [a,b,c,d]: print(L)

"""
isMagicSquare
http://www.kosbie.net/cmu/fall-15/15-112/notes/hw5.html
"""
def isMagicSquare(A): 
    return 42 # write your solution here!  

square1 = [ [ 1, 2, 3 ] , [ 4, 5 ], [ 6 ], [ 7, 8, 9, 10 ] ]
square4 = [ [2, 7, 6],
            [9, 5, 1],
            [4, 3, 8] ]
square5 = [ [2, 7, 6], 
            [9, 8, 1], 
            [8, 3, 8] ]
square6 = [ [5, 5, 5], [5, 5, 5], [5, 5, 5] ]
square7 = [ ["I", 5, 6],
            [9, "am", 1],
            [4, 3, "Batman"] ]

def testIsMagicSquare():
    print("Testing isMagicSquare()...", end="")
    assert(isMagicSquare(square1) == False)
    assert(isMagicSquare([]) == False)
    assert(isMagicSquare([10]) == False)
    assert(isMagicSquare([[]]) == False)
    assert(isMagicSquare([[42]]) == True)  
    assert(isMagicSquare(square4) == True)
    assert(isMagicSquare(square5) == False)
    assert(isMagicSquare(square6) == False) 
    assert(isMagicSquare(square7) == False) 
    assert(isMagicSquare([[8, 1, 6], [3, 5, 7], [4, 9]]) == False)
    print("Passed.")

# testIsMagicSquare() # uncomment to test your function! 
