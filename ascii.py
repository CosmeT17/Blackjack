# TESTING -------------------------------------------------------------------------
# import random
from replit import clear
from readchar import readkey
# ---------------------------------------------------------------------------------
digits = [
    [
        "  __  ",
        " /  \ ",
        "| () |",
        " \__/ "
    ],
    [
        " _ ",
        "/ |",
        "| |",
        "|_|"
    ],
    [
        " ___ ",
        "|_  )",
        " / / ",
        "/___|"
    ],
    [
        " ____",
        "|__ /",
        " |_ \\",
        "|___/"
    ],
    [
        " _ _  ",
        "| | | ",
        "|_  _|",
        "  |_| "
    ],
    [
        " ___ ",
        "| __|",
        "|__ \\",
        "|___/"
    ],
    [
        "  __ ",
        " / / ",
        "/ _ \\",
        "\___/"
    ],
    [
        " ____ ",
        "|__  |",
        "  / / ",
        " /_/  "
    ],
    [
        " ___ ",
        "( _ )",
        "/ _ \\",
        "\___/"
    ],
    [
        " ___ ",
        "/ _ \\",
        "\_, /",
        " /_/ "
    ],
    [
        "   ",
        "   ",
        " _ ",
        "( )",
        "|/ "
    ]
]

def get_int(num, smush = False, comma = True):
    txt = [''] * 4
    ascii = []

    if comma: num = "{:,}".format(num)
    else: num = str(num)

    for digit in num: 
        ascii.append(digits[int(digit)].copy())

    for pos in range(len(ascii)):
        l_digit = ascii[pos]

        if pos != len(num) - 1:
            r_digit = ascii[pos + 1]
            gaps = []
            for line in range(len(digits[0])):
                l_gap = len(l_digit[line]) - len(l_digit[line].rstrip(' '))
                r_gap = len(r_digit[line]) - len(r_digit[line].lstrip(' '))
                gaps.append(l_gap + r_gap)
            gap = min(gaps)
            if smush: gap += 1
        else: gap = -1
        
        for line_num in range(len(l_digit)):
            line = list(l_digit[line_num])

            for _ in range(gap):
                if line[-1] == ' ': line.pop()
                else:
                    if smush:
                        l_char = line[-1]
                        r_char = r_digit[line_num][0]
                        
                        if r_char != ' ' and l_char != ')': line[-1] = r_char
                            
                    r_digit[line_num] =r_digit[line_num][1:]
            txt[line_num] += ''.join(line)
    return txt

# ---------------------------------------------------------------------------------
# TESTING get_int():

def prt(x): 
    for i in x: print(i)

prt(get_int(2674, comma = True))

# prt(get_int(123, True))

# for i in range(10):
#     for j in range(10):
#         clear()
#         prt(get_int(f"{i}{j}"))
#         prt(get_int(f"{i}{j}", True))
#         readkey()

# num = random.randrange(1000000000000)
# clear()
# prt(get_int(num))
# prt(get_int(num, True))
# ---------------------------------------------------------------------------------
