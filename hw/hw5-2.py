########################################
# Name:                                #
# Andrew ID:                           #
# Section:                             #
########################################



####################
# Question 0       #
# Study the notes! #
####################

'''
Carefully go over the recursion examples seen in class and recitation.
Make sure that you are able to reproduce the solutions by yourself.
This will help you a lot with the homework and the exam!!! 
'''



##################################
# Question 1                     #
# Reasoning about recursive code #
##################################

# Do "Reasoning About (Recursive) Code" from 
# http://www.kosbie.net/cmu/fall-11/15-112/handouts/hw5.html#Reasoning

# Put your answers below in a triple-quoted string.

'''
Answers go here.
'''



############################
# Question 2               #
# No loops, only recursion #
############################

# Complete the functions below. Your solutions must be completely recursive.
# In particular, you will not receive any points if you use a "for" loop
# or a "while" loop.

'''
Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
and interleaves their characters starting with the first character in s1. 
For example, interleave('pto', 'yhn') would return the string "python". 
If one string is longer than the other, concatenate the rest of the 
remaining string onto the end of the new string. 
For example, ('a#', 'cD!f2') would return the string "ac#D!f2".
'''

def interleave(s1, s2):
    pass


'''
This function takes a positive integer n as input. It returns a string 
of the form "1 1 2 1 2 3 1 2 3 4 1 2 3 4 5 ...... 1 2 3 4 5 6 7 8...n".
For example, if n is 4, it should return "1 1 2 1 2 3 1 2 3 4".
'''

def foo(n):
    pass


'''
In class we saw an example of a non-destructive reverse function.
Write the same function, but this time make it destructive.
'''

def reverse(L):
    pass


'''
The function removeDuplicates(s) takes a string s as input. 
If there is any character that repeats itself consecutively, 
it deletes the repeated copies. For example, if the input is "abccdeeef", 
the function returns "abcdef".
'''

def removeDuplicates(s):
    pass


'''
Write the recursive function flatten(L), which takes a list 
which may contain lists (which themselves may contain lists, and so on), 
and returns a single list (which does not contain any other lists) 
which contains each of the non-lists, in order, from the original list. 
This is called flattening the list. For example:
flatten([1,[2]]) returns [1,2]
flatten([1,2,[3,[4,5],6],7]) returns [1,2,3,4,5,6,7]
flatten(['wow', [2,[[]]], [True]]) returns ['wow', 2, True]
flatten([]) returns []
flatten([[]]) returns []
flatten(3) returns 3 (not a list)
'''

def flatten(L):
    pass


'''
Write the function isPerfectNumber that takes a possibly-negative integer n 
and returns True if it is a perfect number and False otherwise, 
where a number is perfect if it is the sum of its positive divisors less than itself. 
We'll assume 0 is perfect.
The next perfect number is 6 because 6 = 1 + 2 + 3. 
The next one is 28 because 28 = 1 + 2 + 4 + 7 + 14. 
The next one is 496, then 8128, ...
'''

def isPerfectNumber(n):
    pass



################
# Question 3   #
# Backtracking #
################

'''
Modify the solve(n, m, constraints) function seen in class
(for the nQueens problem) so that instead of returning a solution,
it returns the total number of solutions.'''

def count(n, m, constraints):
    pass


'''
Background: we will say that a board is a square 2d list of integers. 
As with mazes, a solution is a path from the left-top to the right-bottom, 
only here we will only allow moves that are up, down, left and right (no diagonals). 
A solution is an "increasing path" (a coined term) if each value 
on the solution path is strictly larger than the one before it on that path. 
Consider this board:
    board = [[ 1, 3, 2, 4 ],
             [ 0, 4, 0, 3 ],
             [ 5, 6, 8, 9 ],
             [ 0, 7, 8, 9 ]]
This board has exactly one increasing path: 
right to 3, down to 4, down to 6, down to 7, right to 8, right to 9.
With this in mind, write the function increasingPathCount(board) 
that takes such a board and returns the number of increasing paths 
running from the left-top to right-bottom in that board. 
For the example board above, your function would return 1. 
Similarly, consider this board:
    board = [ [3, 5],
              [4, 7] ]
For this board, your function would return 2:
those paths being right,down and also down,right.
Your solution must be recursive (but you can use iteration too).
Also, you cannot simply explore every possible path to solve this problem.
'''

def increasingPathCount(board):
    pass



##############
# Question 4 #
# H-fractal  #
##############

'''
Do Question 6 from here: https://www.cs.cmu.edu/~112/notes/hw9.html
Please follow the directions given in the hint:
"The H that is drawn right in the middle should always have the same size 
(the width and height should be half the window width and height). 
At each level, we draw new H's with half the dimensions of the previous level. 
This is why the window size never has to change 
(since 1 + 1/2 + 1/4 + 1/8 + ... = 2)."
The pictures in mathworld.wolfram.com are misleading!
At each level, the largest H in the middle should have the same size.
'''

from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

def Hfractal():
    run(600,600)



################################
# Question 5: BONUS            #
# A variant of Towers of Hanoi #
################################

'''
Even though this question is bonus, it is highly recommended that you do it.
It is not a hard problem. 

Background: Here, we will consider a modified form of the Towers of Hanoi problem. 
Given an input n>0, there are 2n discs of increasing size 
(instead of just n discs of increasing size). 
There are 3 poles as in the original problem (Pole 0, Pole 1, and Pole 2). 
We label the discs with numbers {1, 2, 3, ..., 2n}, where the label of a disc 
corresponds to its size. Initially, the odd-numbered discs 
(i.e. the discs {1, 3, 5, ..., 2n-1}) are on Pole 0, and the even-numbered discs 
(i.e. the discs {2, 4, 6, ..., 2n}) are on Pole 2. 
The goal is to get all the discs on Pole 1 (the middle pole). 

With this in mind, write the function twoStackHanoi(n) that takes 
a positive int n and returns a list of the moves in order required to solve 
a 2-stack Hanoi problem as described above (so, to ultimately move the n discs 
from Pole 0 and the n other discs from Pole 2 all to Pole 1, while also maintaining 
the Hanoi rule that no disc can be placed on a smaller disc). 
A "move" will be represented as a tuple (x,y), where x and y are both in the set 
{0,1,2}, and means to move one disc from Pole x to Pole y.

Note that we don't care about the efficiency of your solution, 
so it is ok if your solution produces redundant moves.
'''

def twoStackHanoi(n):
    pass
