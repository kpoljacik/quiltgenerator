import turtle
import math

#this file contains functions that are used in drawing both types of blocks

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_qst(size):
    turtle.left(45)
    turtle.forward(math.hypot(size,size))
    turtle.left(135)
    turtle.forward(size)
    turtle.left(135)
    turtle.forward(math.hypot(size,size))


def sawtooth(size):
    turtle.left(135)
    turtle.forward(math.hypot(size,size))
    turtle.right(90)
    turtle.forward(math.hypot(size,size))
