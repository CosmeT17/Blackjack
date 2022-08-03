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
    ascii = digits.copy()
    num = str(num)
    txt = [''] * 4
    
    for digit in range(len(num)):
        l_digit = ascii[int(num[digit])]
        
        if digit != len(num) - 1:
            r_digit = ascii[int(num[digit + 1])]

            gaps = []
            for line in range(len(ascii[0])):
                l_gap = len(l_digit[line]) - len(l_digit[line].rstrip(' '))
                r_gap = len(r_digit[line]) - len(r_digit[line].lstrip(' '))
                gaps.append(l_gap + r_gap)
            gap = min(gaps) + 1
            
        else: gap = -1


# -----------------------------------------------------------
        for line_num in range(len(l_digit)):
            line = list(l_digit[line_num])
            
            for _ in range(gap):
                if line[-1] == ' ': line.pop()
                else:
                    l_char = line[-1]
                    r_char = r_digit[line_num][0]

                    # Left replaces Right:
                    if r_char == ' ' or l_char == ')' or (l_char, r_char) == ('\\', '|'):
                        pass

                    # Right replaces Left:
                    else: line[-1] = r_char

            txt[line_num] += ''.join(line)
          

    return txt

test = get_number(23)
for i in test: print(i)

# def smallest_gap(num_1, num_2):
#     gaps = []
#     for line in range(len(digits[0])):
#         l_gap = len(num_1[line]) - len(num_1[line].rstrip(' '))
#         r_gap = len(num_2[line]) - len(num_2[line].lstrip(' '))
#         gaps.append(l_gap + r_gap)    
#     return min(gaps)
