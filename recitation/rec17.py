"""
listFile(path)
write the recursive function listFiles(path), which takes a string specifying a 
path to a folder and returns list of files in that folder (and all its 
subfolders). Do not count folders (or subfolders) as files. Do not worry if the 
supplied path is not valid or is not a folder. 

To test your function, first download the sample files here 
http://www.kosbie.net/cmu/fall-16/15-112/notes/sampleFiles.zip
Then unzip the folder and move the unzipped folder to the same directory as 
this python file 
"""
import os

def listFiles(path):
    return 42 # implement your solution here! 

def testListFile(): 
    print("Testing listFile...", end="")
    files = ['sampleFiles/emergency.txt', 'sampleFiles/folderA/fishing.txt', 
    'sampleFiles/folderA/folderC/folderD/misspelled.txt', 
    'sampleFiles/folderA/folderC/folderD/penny.txt', 
    'sampleFiles/folderA/folderC/folderE/tree.txt', 
    'sampleFiles/folderA/folderC/giftwrap.txt', 
    'sampleFiles/folderA/widths.txt', 'sampleFiles/folderB/folderH/driving.txt', 
    'sampleFiles/folderB/restArea.txt', 'sampleFiles/mirror.txt']
    assert(listFiles("sampleFiles") == files)
    print("Passed!")

# testListFile() # uncomment to test your function! 


"""
Sierpinksy Carpet 
Similar to Sierpinsky triangle, write the drawSierpinskyCarpet function that 
will produce the following carpet: 
http://mathforum.org/advanced/robertd/carpet.gif
"""
from tkinter import *

def init(data):
    data.level = 1

def drawSierpinskyCarpet(canvas, x, y, size, level):
    pass # implement your solution here! 

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def redrawAll(canvas, data):
    drawSierpinskyCarpet(canvas, 25, 50, 450, data.level)
    canvas.create_text(250, 20,
                       text = "Level %d Sierpinsky Triangle" % (data.level),
                       font = "Arial 26 bold")
    canvas.create_text(250, 40,
                       text = "Use arrows to change level",
                       font = "Arial 10")

def mousePressed(event, data): pass

def timerFired(data): pass

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

# run(500, 500) # uncomment to see your Sierpinsky Carpet