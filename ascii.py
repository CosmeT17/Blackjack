from replit import clear
from readchar import readkey

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
]

def get_number(num, smush = False):
    txt = [''] * 4
    num = str(num)
    ascii = []

    # TESTING
    # r_digit = ''
    
    for digit in num: 
        ascii.append(digits[int(digit)].copy())
    
    for pos in range(len(ascii)):
        
        # for num in ascii:
        #     for line in num: print(line)
        # readkey()
        # clear()
        
        l_digit = ascii[pos]

        if pos != len(num) - 1:
            r_digit = ascii[pos + 1]
            gaps = []
            for line in range(len(digits[0])):
                l_gap = len(l_digit[line]) - len(l_digit[line].rstrip(' '))
                r_gap = len(r_digit[line]) - len(r_digit[line].lstrip(' '))
                gaps.append(l_gap + r_gap)
            gap = min(gaps) + 1
        else: gap = -1

        # print(f"Gap {pos}: {gap}")
        # readkey()
        # clear()
        
        for line_num in range(len(l_digit)):
            line = list(l_digit[line_num])

            # print(f"Left Line {line_num}: {line}")
            # print(f"Right Line {line_num}: {r_digit[line_num]}")
            # readkey()

            for _ in range(gap):
                if line[-1] == ' ': 
                    line.pop()
                else:
                    l_char = line[-1]
                    r_char = r_digit[line_num][0]

                    # print(f"Left Char: {l_char}")
                    # print(f"Right Char: {r_char}")
                    # readkey()
                    
                    
                    if r_char != ' ' and l_char != ')': line[-1] = r_char
                    

                    # print(f"\nERROR:")
                    # print(ascii[pos + 1])
                    # print(ascii[pos + 1][line_num])
                    # print(ascii[pos + 1][line_num][1:])
                    # for num in ascii:
                    #     for line in num: print(line)

                    ascii[pos + 1][line_num] = ascii[pos + 1][line_num][1:]

                    # print(f"\nERROR:")
                    # print(ascii[pos + 1])
                    # print(ascii[pos + 1][line_num])
                    # for num in ascii:
                    #     for line in num: print(line)
                    # readkey()

                # clear()
                # print(f"Modified Left Line {line_num}: {line}")
                # print(f"Modified Right Line {line_num}: {r_digit[line_num]}")
                # readkey()
                # clear()

            txt[line_num] += ''.join(line)

            
            # print("TEXT: ")
            # for line in txt: print(line)
            # readkey()
            # clear()
            
    return txt

def prt(x): 
    for i in x: print(i)


prt(get_number("47398466206"))

# for num in digits:
#     for line in num:
#         print(line)
