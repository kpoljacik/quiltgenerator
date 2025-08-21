import turtle
import tradquiltblocks as trad
import modernquiltblocks as mod
import shared
import random
from time import sleep

HEIGHT = 900
WIDTH = 700
ALL_BLOCKS = mod.modern_blocks | trad.traditional_blocks #combined dictionaries


def get_user_input(first_iteration): 
    responses = []
    if first_iteration == True: #if it's the first time through the program, print background info
        print()
        print("Hello! This program will print a virtual quilt for you based on a few inputs.")
        print("Please answer the following using the letters A, B, or C to indicate your preference.")
        print("After your quilt generates, come back to the terminal to run the module again or close it.")
        print()
    
    while True:
        block_response = input("Would you like a) modern blocks, b)traditional blocks, or c) a mix of both? ")
        if block_response.upper() not in ('A', 'B','C'):
            print("Invalid response. Please type A, B, or C")
        else:
            break
    
    while True:
        grid_response = input("Would you like the quilt grid to be a) 2x2, b) 2x3, or c) 3x3? ")
        if grid_response.upper() not in ('A', 'B','C'):
            print("Invalid response. Please type A, B, or C")
        else:
            break

    while True:
        difficulty_response = input("Would you like the block difficulty to be a) easy only, b) easy or intermediate, or c) all levels? ")
        if difficulty_response.upper() not in ('A', 'B','C'):
            print("Invalid response. Please type A, B, or C")
        else:
            break

    print()

    uniqueness = False
    if block_response.upper() == 'C' and difficulty_response.upper() == 'C':
        print("With these parameters, your quilt can have all unique blocks.")
        while True:
            uniqueness = input("Would you like to try this? Type 'yes' or 'no'. Please note: typing 'no' does not guarantee there will be repeated blocks, it's random! ")
            if uniqueness.upper() not in ('YES', 'NO'):
                print("Invalid response. Please type yes or no. ")
            else:
                break
        if uniqueness.upper() == 'YES':
            uniqueness = True

    responses.extend([block_response.upper(), grid_response.upper(), difficulty_response.upper(), uniqueness])
    return responses


def determine_difficulty(responses):
    difficulty_response = responses[2]
    if difficulty_response == 'A': #easy only
        difficulty = 1
    elif difficulty_response == 'B': #easy or medium
        difficulty = 2
    else: #all levels
        difficulty = 3
    return difficulty


def determine_blocks(responses, difficulty): #pass in difficulty to weed out blocks
    block_type_response = responses[0]
    if block_type_response == 'A': #modern only
        available_blocks = list(mod.modern_blocks.values())
    elif block_type_response == 'B': #traditional only
        available_blocks = list(trad.traditional_blocks.values())
    else: #both modern and traditional blocks
        available_blocks = list(ALL_BLOCKS.values()) #combined dictionaries
    
    filtered_blocks = []

    for block in available_blocks:
        if block["difficulty"] <= difficulty:
            filtered_blocks.append(block)

    return filtered_blocks


def determine_blocksize(responses): #returns number of columns and rows [c, r] based on grid size
    grid_response = responses[1]
    grid_specs = []
    if grid_response == 'A':
        grid_specs = [2, 2]
    elif grid_response == 'B': 
        grid_specs = [2, 3]
    else: 
        grid_specs = [3, 3]

    return grid_specs


def draw_block(block, size):
    block["render"](size) #access the function for the block and pass in the size variable


def render_quilt(available_blocks, grid_specs, uniqueness): 
    size = 200 #size of the blocks
    rows, columns = grid_specs
    row_buffer = (WIDTH - (size * rows))/2
    column_buffer = (HEIGHT-(size*columns))/2
    initial_x = -(WIDTH/2)+row_buffer #finding the x_coord by taking the full width divided by two and adding a buffer
    initial_y = (HEIGHT/2)-column_buffer-size #finding the y_coord by taking the full width divided by two, adding a buffer and the size of the block so it doesn't go off screen
    turtle.penup()
    turtle.goto(initial_x, initial_y)
    turtle.pendown()
    
    picked_blocks = set()
    for column in range(columns): 
        for row in range(rows):
            random_block = random.choice(available_blocks)
            if uniqueness == True:
                while True:
                    if random_block['name'] not in picked_blocks:
                        picked_blocks.add(random_block['name'])
                        break
                    random_block = random.choice(available_blocks)

            print(f"Now printing block: {random_block['name']}")
            turtle.setheading(0)
            turtle.penup()
            turtle.goto(initial_x + (size*row), initial_y - (size*column))
            turtle.pendown()
            shared.draw_square(size)
            draw_block(random_block, size)


def run_program(iteration):
    #get user responses and generate quilt based on these parameters
    responses = get_user_input(iteration)
    uniqueness = responses[3]
    difficulty = determine_difficulty(responses)
    availble_blocks = determine_blocks(responses, difficulty)
    grid_specs = determine_blocksize(responses)

    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    turtle.TurtleScreen._RUNNING=True #need to set turtle screen to run again when rerunning module without exiting
    turtle.speed(8)

    render_quilt(availble_blocks, grid_specs, uniqueness)
    turtle.hideturtle()

    sleep(7) #delay for 7 seconds before closing the window
    turtle.bye()


def main():
    first_iteration = True
    run_program(first_iteration)
    print()
    while True:
        action = input("To run this program again, type 'Go', otherwise type 'Exit'. ")
        if action.upper() == 'EXIT':
            print("Thank you! Goodbye.")
            break
        elif action.upper() == 'GO':
            print("Running again...")
            print()
            first_iteration = False
            run_program(first_iteration)
        else:
            print("Invalid response. To run this program again, type 'Go', otherwise type 'Exit'. ")


main()
