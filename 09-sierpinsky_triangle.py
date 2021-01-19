from tkinter import *
import random
import math


def plotpoint(x, y):
    global canvas
    #     point = canvas.create_line(x-1, y-1, x+1, y+1, fill = "#000000")
    point = canvas.create_oval(x, y, x, y, fill="#000000", outline="#000000")


x = 0  # Initial coordinates
y = 0
# x and y will always be in the interval [0, 1]
mod = int(input("What is the modulo of the Sierpinsky triangle that you want to generate? (try:3)"))
points = int(input("How many points do you want the triangle to have? (try:100.0000"))
tkengine = Tk()  # Window in which the triangle will be generated
window = Frame(tkengine)
window.pack()
# The dimensions of the canvas make the triangle look equilateral
canvas = Canvas(window, height=700, width=808, bg="#FFFFFF")
canvas.pack()
for t in range(points):
    # Procedure for placing the points
    while True:
        # First, randomly choose one of the mod(mod+1)/2 triangles of the first step. a and b are two vectors which point to the chosen triangle. a goes one triangle to the right and b one up-right. The algorithm gives the same probability to every triangle, although it's not efficient.
        a = random.randint(0, mod - 1)
        b = random.randint(0, mod - 1)
        if a + b < mod:
            break
    # The previous point is dilated towards the origin of coordinates so that the big triangle of step 0 becomes the small one at the bottom-left of step one (divide by modulus). Then the vectors are added in order to move the point to the same place in another triangle.
    x = x / mod + a / mod + b / 2 / mod
    y = y / mod + b / mod
    # Coordinates [0,1] converted to pixels, for plotting in the canvas.
    X = math.floor(x * 808)
    Y = math.floor((1 - y) * 700)
    plotpoint(X, Y)
tkengine.mainloop()
