# makeBlackAndWhite.py

from tkinter import *

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def getRGB(image, x, y):
    value = image.get(x, y)
    return tuple(map(int, value.split(" ")))

def setRGB(image, x, y, red, green, blue):
    color = rgbString(red, green, blue)
    image.put(color, to=(x,y))
    
def makeBlackAndWhite(image):
    for x in range(image.width()):
        for y in range(image.height()):
            (r, g, b) = getRGB(image, x, y)
            gray = (r + g + b)/3
            bw = 0 if (gray < 128) else 255
            setRGB(image, x, y, bw, bw, bw)


def init(data):
    data["image"] = PhotoImage(file="publicImage.gif")
    
def mousePressed(event, data):
    pass

def keyPressed(event, data):
    makeBlackAndWhite(data["image"])

def timerFired(data):
    pass

def redrawAll(canvas, data):
    text = "Press a key to change to black and white."
    canvas.create_text(data["width"]/2, 10, text=text)
    canvas.create_image(data["width"]/2, data["height"]/2, image=data["image"])

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
        canvas.after(data["timerDelay"], timerFiredWrapper, canvas, data)
    # Set up data and call init
    root = Tk()
    data = dict()
    data["width"] = width
    data["height"] = height
    data["timerDelay"] = 100 # milliseconds
    init(data)
    # create the root and the canvas
    
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

run(600, 600)
