"""
    File: pipe_picture_practice.py
    Author: Xin Li
    Purpose: In this project i will draw a single picture of a
            set of pipes.

"""
from graphics import graphics

def pipe(gui):
    gui.rectangle(0, 0, 600, 600, 'gray')

    #pipe(0,0)
    gui.line(100, 100, 200, 100, 'black', 20)
    gui.line(100, 90, 100, 200, 'black', 20)

    #pipe(0,1)
    gui.line(200, 100, 400, 100, 'black', 20)
    gui.line(300, 0, 300, 100, 'black', 20)
    gui.rectangle(265, 65, 70, 70, 'black',)
    gui.line(200, 100, 400, 100, 'blue', 10)
    gui.line(300, 0, 300, 100, 'blue', 10)
    gui.rectangle(275, 75, 50, 50, 'blue',)

    #pipe(0,1)
    gui.line(100, 200, 100, 400, 'black', 20)
    gui.line(0, 300, 200, 300, 'black', 20)

    #pipe(1,1)
    gui.line(200, 300, 400, 300, 'black',20)
    gui.line(200, 300, 400, 300, 'blue', 10)

    #pipe(2,1)
    gui.line(500, 200, 500, 400, 'black', 20)
    gui.rectangle(475, 275, 50, 50,'black')

    #pipe(0,2)
    gui.line(100, 400, 100, 510, 'black', 20)

    #pipe(1,2)
    gui.line(200, 500, 400, 500, 'black', 20)

    #pipe(2,2)
    gui.line(400, 500, 600, 500, 'black', 20)

    #wall_line
    gui.line(200, 0, 200, 600, 'silver', 10)
    gui.line(400, 0, 400, 600, 'silver', 10)
    gui.line(0, 200, 600, 200, 'silver', 10)
    gui.line(0, 400, 600, 400, 'silver', 10)

def main():
# Create the canvas
    gui = graphics(600, 600, 'Pipe Grid')
    pipe(gui)
main()
© 2021 GitHub, Inc.
