# events-example2.py
# Demos timer, mouse, and keyboard events

from tkinter import *


# MODEL VIEW CONTROLLER (MVC)
####################################
# MODEL:       the data
# VIEW:        redrawAll and its helper functions
# CONTROLLER:  event-handling functions and their helper functions
####################################


####################################
# customize these functions
####################################


# Initialize the data which will be used to draw on the screen.
def init(data):
    data.squareLeft = 50
    data.squareTop = 120
    data.squareSize = 100
    data.circleR = 20
    data.squareFill = "yellow"
    data.circleCenters = [ ]
    data.timerDelay = 250


# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    newCircleCenter = (event.x, event.y)
    data.circleCenters.append(newCircleCenter)

def keyPressed(event, data):
    if (event.char == "d"):
        if (len(data.circleCenters) > 0):
            data.circleCenters.pop(0)
        else:
            print("No more circles to delete!")
    if (event.keysym == "Left"):
        sqRight = data.squareLeft + data.squareSize
        if (sqRight > 0):
            data.squareLeft -= 20
        else:
            data.squareLeft = data.width

def timerFired(data):
    data.squareFill = "green" if (data.squareFill == "yellow") else "yellow"


# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.
def redrawAll(canvas, data):
    # draw the square
    canvas.create_rectangle(data.squareLeft, data.squareTop,
                            data.squareLeft + data.squareSize, 
                            data.squareTop + data.squareSize,
                            fill=data.squareFill)
    # draw the circles
    r = data.circleR
    for circleCenter in data.circleCenters:
        (cx, cy) = circleCenter
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")
    # draw the text
    canvas.create_text(data.width/2, 20, text="events-example2.py")
    canvas.create_text(data.width/2, 40, text="Mouse clicks create circles")
    canvas.create_text(data.width/2, 60, text="Pressing 'd' deletes circles")
    canvas.create_text(data.width/2, 80, text="Left arrow moves square left")
    canvas.create_text(data.width/2, 100, text="Timer changes color of square")

####################################
####################################
# use the run function as-is
####################################
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

run(300, 600)
