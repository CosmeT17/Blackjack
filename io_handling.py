# Contains functions useful for manipulating inputs and outputs

from readchar import readkey
from os import system

# Arrow Keys
UP = "\x1b\x5b\x41"    # Up Arrow "\x1b[A"
DOWN =  "\x1b\x5b\x42" # Down Arrow "\x1b[B"
RIGHT = "\x1b\x5b\x43" # Right Arrow "\x1b[C"
LEFT = "\x1b\x5b\x44"  # Left Arrow "\x1b[D" 

# Prints str without a newline
prt = lambda str: print(str, end = '', flush = True)

# Clears the console
def clear():
    "Clears the console."
    system('clear')

# Clears the line the cursor's on
def clear_line(length):
    '''Clears the line from right to left at the cursor's position.
    The cursor must be positioned at the end of the line.
    
    \tint length: The length of the line to be deleted'''
    prt(f"{LEFT} {LEFT}" * length)

# Clears the specified lines from the console
def clear_lines(length, num_lines, del_current_line = True):
    '''Clears the specified lines from the console.
    Clears the lines above and at the cursor's position.
    To delete the current line, the cursor must be at 
    the end of the line.
    
    \tint length: The length of the lines
    
    \tint num_lines: How many lines are to be deleted
    
    \tbool del_current_line: If true, deletes the current line'''
    
    if del_current_line: print()
    for line in range(num_lines): prt(UP + ' ' * length + LEFT * length)

# Moves the cursor to the coordinates
def move_cursor(x, y,):
    '''Moves the cursor to the given coordinates.
    
    The coordinates are in reference to the cursor's current position.
    
    \tPositive x: Move x spaces to the right
    
    \tNegative x: Move x spaces to the left
    
    \tPositive y: Move y lines upwards
    
    \tNegative y: Move y lines downwards'''
    
    if y > 0: prt(UP * y)
    elif y < 0: prt(DOWN * -y)
    
    if x > 0: prt(RIGHT * x)
    elif x < 0: prt(LEFT * -x)

# Returns the pressed key if it is in the options list
def get_keypress(prompt, options):
    '''Prints the prompt and waits for the user to press any of
    the keys in the options list.
    
    Once a key that's in the list is pressed, it is returned.
    Nothing happens otherwise.'''
    
    prt(prompt)
    keypress = readkey().upper()
    while keypress not in options: keypress = readkey().upper()
    return keypress
