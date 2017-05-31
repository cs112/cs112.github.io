###############################################################################
# String CT [10 mins]
###############################################################################
import string
def traceThis():
    s = "he\t" + "l\nl\\\to"
    print(s, len(s))
    
    t = """
by
e"""
    print(len(t), len(t.strip()))
    
    s = ("abc"*3).replace("ca","d")
    print(s, s[1:3], s[:5:2], (s[:5])[-2:-4:-1])

    (s, t) = ("abcbcd", "bc")
    print(s.find(t), s.find(t,2), s.find(t, 4))
    
    for s in ("abc"*3).split("ca"): print(s)
    
    n = 4.2042
    print("L%0.1fO\nL%0.2fO\nL%+8.3fO\nL%-8.3fO" % (n, n, n, n))

traceThis()

###############################################################################
# String ROC [5 mins]
###############################################################################
def roc(s): 
    assert(type(s) == str)
    t = "CBBD"
    for i in range(4):
        print(s.count(s[i]))
        assert(s.count(s[i]) == (ord(t[i]) - ord("A")))
    return (s[::3] == s[5:2:-1])

###############################################################################
# String FR : wordWrap [10 mins]
# Problems here: https://www.cs.cmu.edu/~112/notes/hw3-practice.html#wordWrap
###############################################################################
def wordWrap(text, width):
    return "meme" # replace with your solution

###############################################################################
# Graphics FR: draw Blank Sheet Music [20 mins] 
###############################################################################
from tkinter import *
 
def draw(canvas, width, height):
    pass # replace with your drawing code!
 
def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")
 
runDrawing(800, 200)