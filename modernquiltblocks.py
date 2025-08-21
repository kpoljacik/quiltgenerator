import turtle
import math
import shared

#this file contains all of the code for turtle to draw the modern blocks
#also contains a dictionary with information about the modern blocks

def draw_qst_in_square(size):
    half_size = size/2
    fourth_size = size/4
    turtle.forward(half_size)
    turtle.left(90)
    turtle.penup()
    turtle.forward(fourth_size/2)
    turtle.pendown()
    turtle.right(45)
    shared.draw_square(half_size)
    shared.draw_qst(half_size)


def draw_plus(size):
    third_size = size/3
    sixth_size = size/6
    def small_sawtooth():
        turtle.left(90)
        turtle.forward(math.hypot(sixth_size, sixth_size))
        turtle.right(90)
        turtle.forward(math.hypot(sixth_size, sixth_size))

    def corner():
        turtle.left(90)
        turtle.forward(math.hypot(third_size, third_size))
    
    turtle.left(90)
    turtle.forward(third_size)
    turtle.right(135)
    turtle.forward(math.hypot(third_size, third_size))

    for _ in range(3):
        small_sawtooth()
        corner()
    small_sawtooth()


def half_circle(size): #helper function
    half_size = size/2
    # turtle.left(90)
    turtle.forward(half_size)
    turtle.right(180)
    turtle.circle(half_size, 180)


def half_circle_with_diameter(size): #helper function
    half_circle(size)
    turtle.left(90)
    turtle.forward(size)


def draw_double_half_moon(size):
    turtle.left(90)
    half_circle_with_diameter(size)
    turtle.right(90)
    half_circle(size)


def draw_half_circle_triangle(size):
    half_size = size/2
    turtle.left(90)
    half_circle_with_diameter(size) 
    turtle.right(90)
    turtle.forward(half_size)
    turtle.right(135)
    turtle.forward(math.hypot(half_size,half_size))
    turtle.left(90)
    turtle.forward(math.hypot(half_size,half_size))


def draw_scallops(size):
    sixth_size = size/6
    for _ in range(3):
        turtle.circle(sixth_size, 180)
        turtle.right(180)
    turtle.forward(size)
    turtle.left(180)
    for _ in range(3):
        turtle.circle(sixth_size, 180)
        turtle.left(180)


def draw_tulip(size):
    half_size = size/2
    turtle.left(90)
    half_circle(size)
    turtle.forward(half_size)
    turtle.left(90)
    turtle.circle(half_size, 90)
    turtle.right(180)
    turtle.circle(half_size, 90)


def draw_orange_peel(size):
    half_size = size/2
    for _ in range(4):
        turtle.circle(half_size, 90)
        turtle.left(90)
        turtle.circle(half_size, 90)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)


def draw_circle_tile(size):
    half_size = size/2
    fourth_size = size/4
    turtle.forward(half_size)
    turtle.left(90)
    for _ in range(4):
        turtle.forward(fourth_size)
        turtle.right(90)
        turtle.circle(fourth_size, 90)
        turtle.right(90)
        turtle.forward(fourth_size)
        turtle.right(180)
    

def draw_modern_star(size):
    half_size = size/2
    turtle.forward(half_size)
    turtle.left(90)
    for _ in range(4):
        turtle.circle(half_size, 90)
        turtle.right(180)


modern_blocks = {
    "plus-block": {
        "id": 1,
        "name": "plus",
        "difficulty": 1,
        "render": draw_plus
    },

    "qst-square-block": {
        "id": 2,
        "name": "quarter-square triangles inside inner square",
        "difficulty": 1,
        "render": draw_qst_in_square
    },

    "half-moon-block": {
        "id": 3,
        "name": "double half-moon",
        "difficulty": 2,
        "render": draw_double_half_moon
    },
    "half-circle-block": {
        "id": 4,
        "name": "half-circle triangle",
        "difficulty": 2,
        "render": draw_half_circle_triangle
    },

    "scallop-block": {
        "id": 5,
        "name": "scallops",
        "difficulty": 3,
        "render": draw_scallops
    },

    "tulip-block": {
        "id": 6,
        "name": "tulip",
        "difficulty": 3,
        "render": draw_tulip
    },

    "orange-peel-block": {
        "id": 7,
        "name": "orange peel",
        "difficulty": 3,
        "render": draw_orange_peel
    },

    "circle-tile-block": {
        "id": 8,
        "name": "circle tile",
        "difficulty": 3,
        "render": draw_circle_tile
    },

    "star-block": {
        "id": 9,
        "name": "modern star",
        "difficulty": 3,
        "render": draw_modern_star
    }

}

