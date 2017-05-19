from tkinter import *
import random


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
    # data already has data.width, data.height, data.timerDelay
    data["circles"] = []


# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    r = random.randint(0, 100)
    color = random.choice(["red", "blue", "green", "purple", "cyan"])
    circle = {"x": event.x, "y": event.y, "r": r, "color": color}
    data["circles"].append(circle)

def keyPressed(event, data):
    if(event.keysym == "d"):
        data["circles"].pop()

def timerFired(data):
    for circle in data["circles"]:
        circle["y"] = (circle["y"] + 10) % data["height"]


# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.
def redrawAll(canvas, data):
    for circle in data["circles"]:
        canvas.create_oval(circle["x"]-circle["r"], circle["y"]-circle["r"], 
                           circle["x"]+circle["r"], circle["y"]+circle["r"], 
                           fill=circle["color"])



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
        canvas.after(data["timerDelay"], timerFiredWrapper, canvas, data)
    # Set up data and call init
    data = dict()
    data["width"] = width
    data["height"] = height
    data["timerDelay"] = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data["width"], height=data["height"])
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

run(800, 400)