# ASCII art digits + comma
digits = {
    '0': ["  __  ",
          " /  \ ",
          "| () |",
          " \__/ "],
    '1': [" _ ",
          "/ |",
          "| |",
          "|_|"],
    '2': [" ___ ",
          "|_  )",
          " / / ",
          "/___|"],
    '3': [" ____",
          "|__ /",
          " |_ \\",
          "|___/"],
    '4': [" _ _  ",
          "| | | ",
          "|_  _|",
          "  |_| "],
    '5': [" ___ ",
          "| __|",
          "|__ \\",
          "|___/"],
    '6': ["  __ ",
          " / / ",
          "/ _ \\",
          "\___/"],
    '7': [" ____ ",
          "|__  |",
          "  / / ",
          " /_/  "],
    '8': [" ___ ",
          "( _ )",
          "/ _ \\",
          "\___/"],
    '9': [" ___ ",
          "/ _ \\",
          "\_, /",
          " /_/ "],
    ',': ["   ",
          "   ",
          " _ ",
          "( )",
          "|/ "]
}

# Returns an integer as ASCII art
def get_int(num, smush = False, comma = False):
    '''Returns the positive integer num as an ASCII art list.
    
    The list is composed of strings, each element being 
    a line in the ASCII art.
    
    If smush is True, the digits are compacted closer together.
    
    If comma is True, then a comma will be added to every 
    thousand places starting from left.'''
    
    txt = [''] * 5 if comma else [''] * 4
    absorb_comma = False
    ascii = []

    # Casting the int num to str, adding commas if needed
    if comma: num = "{:,}".format(num)
    else: num = str(num)

    # Appending the ASCII digits of num to the list ascii
    for digit in num: ascii.append(digits[digit].copy())

    # Appending an extra empty line to ascii if comma is True
    if comma: 
        for pos in range(len(ascii)):
            if num[pos] != ',': 
                ascii[pos].append(' ' * len(ascii[pos][0]))
    
    for pos in range(len(ascii)):
        l_digit = ascii[pos]

        # Calculating the size of the gap between digits
        if pos != len(num) - 1:
            r_digit = ascii[pos + 1]
            gaps = []
            for line in range(len(digits['0'])):
                l_gap = len(l_digit[line]) - len(l_digit[line].rstrip(' '))
                r_gap = len(r_digit[line]) - len(r_digit[line].lstrip(' '))
                gaps.append(l_gap + r_gap)
            gap = min(gaps)
            if smush: gap += 1
        else: gap = -1

        # If there's a comma after the current digit, it will be absorbed
        if comma and pos < len(ascii) - 1 and num[pos + 1] == ',':
            absorb_comma = True
 
        for line_num in range(len(l_digit)):
            line = list(l_digit[line_num])
            
            for _ in range(gap):
                # Removing the whitespaces in the gaps
                if line[-1] == ' ': line.pop()
                else:
                    # Compacting the digits together where they meet
                    if smush:
                        l_char = line[-1]
                        r_char = r_digit[line_num][0]
                        
                        # Replace left with Right
                        if not comma or r_char != '_':
                            if r_char != ' ' and l_char != ')':
                                if (num[pos], num[pos + 1]) != ('2', '0'):
                                    line[-1] = r_char
                    r_digit[line_num] = r_digit[line_num][1:]

            # Absorb the the comma to the current digit
            if absorb_comma: 
                ascii[pos + 1][line_num] = ''.join(line) + r_digit[line_num]

            # Add the modified line in the ascii list to the txt list
            else: txt[line_num] += ''.join(line)

        # Comma successfully absorbed 
        if absorb_comma: absorb_comma = False
            
    # Return txt, which contains the completed ASCII art
    return txt

# Returns the ASCII art of a poker chip
def poker_chip(num = ''):
    '''Returns the ASCII art of a poker chip as a list.

    The list is composed of strings, each element being 
    a line in the ASCII art.
    
    The value of the chip can be specified with the positive int num.'''

    # The ASCII art for 1000 and 500 are different than
    # the ones produced for get_int() for spacing
    if num == 1000:
        num = [   
            " _  __  __  __  ",
            "/ |/  \/  \/  \ ",
            "| | () |() |() |",
            "|_|\__/\__/\__/ "
        ]
    elif num == 500:
        num = [
            " ___   __   __  ",
            "| __| /  \ /  \ ",
            "|__ \| () | () |",
            "|___/ \__/ \__/ "
        ]

    # Changing num to ASCII art
    else: num = get_int(num)

    # Creating and returning the poker chip
    return [
        "     xxxooooxxx     ",
        "   xox        xox   ",
        " xox            xox ",
        f"xo{num[0].center(16)}ox",
        f"xo{num[1].center(16)}ox",
        f"xo{num[2].center(16)}ox",
        f"xo{num[3].center(16)}ox",
        " xox            xox ",
        "   xox        xox   ",
        "     xxxxxxxxxx     "
    ]

# Creating and storing different valued poker chips
poker_chips = {
    '1': poker_chip(1),
    '2': poker_chip(5),
    '3': poker_chip(25),
    '4': poker_chip(50),
    '5': poker_chip(100),
    '6': poker_chip(500),
    '7': poker_chip(1000),
}

# TESTING poker_chips():
# ---------------------------------------------------------------------------------
# def prt(x): 
#     for i in x: print(i)

# for chip in poker_chips:
#     prt(poker_chips[chip])
#     print()
# # ---------------------------------------------------------------------------------

# TESTING get_int():
# ---------------------------------------------------------------------------------
# from replit import clear
# from readchar import readkey

# def prt(x): 
#     for i in x: print(i)

# prt(get_int(7368753, smush = True, comma = True))

# for i in range(10):
#     for j in range(10):
#         if i == 0: i = 10
#         clear()
        
        # print("No Smush, No Comma:")
        # prt(get_int(int(f"{i}{j}"), smush = False, comma = False))

        # print("Smush, No Comma:")
        # prt(get_int(int(f"{i}{j}"), smush = True, comma = False))

        # print("No Smush, Comma:")
        # prt(get_int(int(f"{i}{j}00"), smush = False, comma = True))

        # print("Smush, Comma:")
        # prt(get_int(int(f"{i}{j}00"), smush = True, comma = True))

        # readkey()
# ---------------------------------------------------------------------------------
