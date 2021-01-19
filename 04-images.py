#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we draw an image
on the canvas.

Author: Jan Bodnar
Website: www.zetcode.com

Requiere intalar PIP y Pillow
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
"""

from tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image, ImageTk


class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("High Tatras")
        self.pack(fill=BOTH, expand=1)

        self.img = Image.open("imagen1.jpg")
        self.imagen1 = ImageTk.PhotoImage(self.img)

        canvas = Canvas(self, width=self.img.size[0] + 20, height=self.img.size[1] + 20)
        canvas.create_image(10, 10, anchor=NW, image=self.imagen1)
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
