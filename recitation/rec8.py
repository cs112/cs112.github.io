"""
IMPORTANT: Before you start this problem, make sure you fully understand the 
wordSearch solution given in the course note. 

Now solve this problem: 
wordSearchWithIntegerWildCards 
Here we will modify wordSearch so that we can include positive integers in the 
board, like so (see board[1][1]):
    board = [ [ 'p', 'i', 'g' ],
              [ 's',   2, 'c' ],
            ]
When matching a word, a positive integer on the board matches exactly that many 
letters in the word. So the board above contains the word "cow" starting from 
[1,2] heading left, since the 2 matches "ow". It also contains the word "cows" 
for the same reason. But it does not contain the word "co", since the 2 must 
match exactly 2 letters. To make this work, of the three functions in our 
wordSearch solution, the outer two do not have to change, but the innermost 
one does. Rewrite the innermost function here so that it works as described. 
Your function should return True if the word is in the wordSearch and False 
otherwise.
"""

def wordSearch(board, word):
    return 42 # place your solution here! 

def testWordSearch():
    print("Testing wordSearch()...", end="")
    board = [ [ 'p', 'i', 'g' ],
              [ 's', 2, 'c' ]
            ]
    assert(wordSearch(board, "cow") == True)
    assert(wordSearch(board, "cows") == True)
    assert(wordSearch(board, "coat") == False)
    assert(wordSearch(board, "pig") == True)
    assert(wordSearch(board, "z") == False)
    assert(wordSearch(board, "zz") == True)
    print("Passed!")

# testWordSearch() # uncomment this line to test! 


