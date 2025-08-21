import turtle
import math
import shared

#this file contains all of the code for turtle to draw the traditional blocks
#also contains a dictionary with information about the traditional blocks
        
def bottom_left_square(distance): #helper function for blocks with squares in corner
    turtle.left(90)
    turtle.forward(distance)
    turtle.right(90)
    turtle.forward(distance)
    turtle.right(90)
    turtle.forward(distance)


def draw_hst(size):
    turtle.left(45)
    turtle.forward(math.hypot(size,size))


def draw_square_in_square(size):
    half_size = size/2
    turtle.forward(half_size)
    turtle.left(45)
    shared.draw_square(math.hypot(half_size, half_size))


def draw_nine_patch(size):
    third_size = size/3
    def row_of_squares():
        for _ in range(3):
            shared.draw_square(third_size)
            turtle.forward(third_size)

    for _ in range(2):
        row_of_squares()
        turtle.left(90)
        turtle.forward(third_size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(180)
    
    row_of_squares()


def draw_sawtooth_square(size):
    fourth_size = size/4
    half_size = size/2
    bottom_left_square(fourth_size)
    #sawtooth
    for _ in range(4):
        shared.sawtooth(fourth_size)
        turtle.left(135)
        turtle.forward(fourth_size)
        turtle.right(90)
        turtle.forward(fourth_size)
    #inner square
    turtle.left(90)
    turtle.forward(half_size)
    turtle.left(90)
    turtle.forward(fourth_size)
    shared.draw_square(half_size)


def draw_shoo_fly(size):
    third_size = size/3
    #bottom left corner triangle
    turtle.forward(third_size)
    turtle.left(135)
    turtle.forward(math.hypot((third_size),(third_size)))
    turtle.right(135)
    turtle.forward(third_size)
    turtle.right(90)
    turtle.forward(third_size)

    #bottom right corner triangle
    for _ in range(2):
        turtle.left(90)
        turtle.forward(third_size)
    turtle.right(90)
    turtle.forward(third_size)
    turtle.right(135)
    turtle.forward(math.hypot((third_size),(third_size)))

    #top right corner
    turtle.left(135)
    turtle.forward(third_size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(third_size)
    turtle.left(135)
    turtle.forward(math.hypot((third_size),(third_size)))
    turtle.right(135)
    turtle.forward(third_size)
    turtle.right(90)
    turtle.forward(third_size)

    #top left corner
    turtle.left(90)
    turtle.forward(third_size)
    turtle.left(45)
    turtle.forward(math.hypot((third_size),(third_size)))
    turtle.left(135)
    turtle.forward(third_size)
    turtle.left(90)
    turtle.forward(third_size)

    #inner square 
    turtle.left(180)
    turtle.forward(third_size)
    shared.draw_square(third_size)


def draw_bear_paw(size):
    third_size = size/3
    turtle.forward((third_size)*2)
    turtle.left(45)

    #right part of bear paw
    turtle.forward(math.hypot(third_size,third_size))
    turtle.left(135)
    turtle.forward(third_size)
    turtle.right(135)
    turtle.forward(math.hypot(third_size,third_size))
    turtle.left(135)
    turtle.forward(third_size)

    #top of paw
    turtle.right(90)
    turtle.forward(third_size)
    turtle.left(135)
    turtle.forward(math.hypot(third_size,third_size))
    turtle.right(135)
    turtle.forward(third_size)
    turtle.left(135)
    turtle.forward(math.hypot(third_size,third_size))

    # #inner square
    turtle.left(135)
    turtle.forward(third_size*2)
    turtle.right(90)
    turtle.forward(third_size*2)


def draw_log_cabin(size):
    fourth_size = size/4
    turtle.left(90)
    for i in range(3, 0, -1):
        turtle.forward(fourth_size)
        turtle.right(90)
        turtle.forward(fourth_size*i)
        turtle.left(90)
        turtle.forward(fourth_size*i)
        turtle.left(180)


def draw_bouquet(size):
    fourth_size = size/4
    turtle.forward(fourth_size*3)
    turtle.left(45)
    turtle.forward(math.hypot(fourth_size, fourth_size))
    turtle.left(135)
    turtle.forward(fourth_size)
    turtle.left(90)
    turtle.forward(fourth_size)
    turtle.left(180)
    turtle.forward(size)

    shared.sawtooth(fourth_size)
    turtle.left(135)
    turtle.forward(fourth_size)
    turtle.right(90)
    turtle.forward(fourth_size)
    shared.sawtooth(fourth_size)

    turtle.left(135)
    turtle.forward(fourth_size*3)

    turtle.penup()
    turtle.left(180)
    turtle.forward(fourth_size*3)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(math.hypot(fourth_size*3, fourth_size*3))


def draw_antique_tile(size):
    third_size = size/3
    sixth_size = third_size/2

    def left_forward():
        turtle.forward(sixth_size)
        turtle.left(90)

    def outside_tile():
        turtle.forward(third_size)
        turtle.left(90)
        turtle.forward(sixth_size)
        turtle.right(90)
        turtle.forward(third_size)
        turtle.right(90)
        turtle.forward(sixth_size)

    outside_tile()

    for _ in range (3):
        turtle.left(90)
        turtle.forward(third_size)
        turtle.left(90)
        outside_tile()

    #bottom left corner square
    turtle.left(180)
    turtle.forward(sixth_size)
    turtle.right(90)
    for _ in range(2):
        left_forward()

    turtle.forward(sixth_size)
    turtle.right(90)

    #bottom right corner square
    turtle.forward(third_size)
    turtle.right(90)
    for _ in range(2):
        left_forward()
    turtle.forward(third_size)

    #top right corner square
    turtle.forward(third_size)
    turtle.left(90)
    left_forward()
    turtle.forward(sixth_size)
    turtle.right(90)
    turtle.forward(third_size)

    #top left corner square
    turtle.right(90)
    for _ in range(2):
        left_forward()
    turtle.forward(third_size/2)

    #inner rectangle
    for _ in range(2):
        turtle.forward(third_size)
        turtle.left(90)
        turtle.forward(third_size*2)
        turtle.left(90)
    
    #inner square
    turtle.left(90)
    turtle.forward(sixth_size)
    turtle.right(90)
    shared.draw_square(third_size)


traditional_blocks = {
    "hst-block": {
        "id": 10,
        "name": "half-square triangle",
        "difficulty": 1,
        "render": draw_hst
    },
    "qst-block": {
        "id": 11,
        "name": "quarter-square triangle",
        "difficulty": 1,
        "render": shared.draw_qst
    },

    "economy-block": {
        "id": 12,
        "name": "square in square",
        "difficulty": 1,
        "render": draw_square_in_square
    },
    
    "nine-patch-block": {
        "id": 13,
        "name": "nine patch",
        "difficulty": 1,
        "render": draw_nine_patch
    },

    "sawtooth-block": {
        "id": 14,
        "name": "sawtooth square",
        "difficulty": 2,
        "render": draw_sawtooth_square
    },

    "bear-paw-block": {
        "id": 15,
        "name": "bear paw",
        "difficulty": 2,
        "render": draw_bear_paw
    },
    
    "log-cabin-block": {
        "id": 16,
        "name": "log cabin",
        "difficulty": 2,
        "render": draw_log_cabin
    },

    "antique-tile-block": {
        "id": 17,
        "name": "antique tile",
        "difficulty": 3,
        "render": draw_antique_tile
    },

    "bouquet-block": {
        "id": 18,
        "name": "bouquet",
        "difficulty": 3,
        "render": draw_bouquet
    }
}


