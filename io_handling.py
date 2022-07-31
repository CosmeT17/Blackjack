from readchar import readkey

# Arrow Keys
UP = "\x1b\x5b\x41"    # Up Arrow "\x1b[A"
DOWN =  "\x1b\x5b\x42" # Down Arrow "\x1b[B"
RIGHT = "\x1b\x5b\x43" # Right Arrow "\x1b[C"
LEFT = "\x1b\x5b\x44"  # Left Arrow "\x1b[D" 

prt = lambda str: print(str, end = '', flush = True)
clear_line = lambda length: prt(f"{LEFT} {LEFT}" * length)

def clear_lines(length,num_lines):
    for line in range(num_lines): 
        prt(UP + ' ' * length + LEFT * length)

def move_cursor(x, y,):
    if y > 0: prt(UP * y)
    elif y < 0: prt(DOWN * -y)
    
    if x > 0: prt(RIGHT * x)
    elif x < 0: prt(LEFT * -x)

def get_keypress(prompt, options):
    prt(prompt)
    keypress = readkey().upper()
    while keypress not in options: keypress = readkey().upper()

    return keypress
