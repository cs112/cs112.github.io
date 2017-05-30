# 15-112, Summer 1, Homework 2.1
######################################
# Full name:
# Andrew ID:
######################################

######################################################################
# Place your non-graphics solutions here!
######################################################################

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your graphics solutions here!
######################################################################
def drawGradient(canvas, x0, y0, x1, y1):
    pass

def drawGrid(canvas, x0, y0, x1, y1):
    pass

######################################################################
# Drivers: do NOT modify this code
######################################################################
from tkinter import *

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,
        fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(170, 50, 570, 450, width=4)
        drawFn(canvas, 170, 50, 570, 450)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, 
            fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawGradient, drawGrid]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in range(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, 
            command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include function calls for your own test functions
    graphicsMain()

if __name__ == "__main__":
     main()