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
    
    for digit in num: ascii.append(digits[int(digit)])
    
    for pos in range(len(ascii)):
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

        for line_num in range(len(l_digit)):
            line = list(l_digit[line_num])

            for _ in range(gap):
                if line[-1] == ' ': line.pop()
                else:
                    l_char = line[-1]
                    r_char = r_digit[line_num][0]
                    
                    if r_char != ' ' and l_char != ')':
                        line[-1] = r_char
                    ascii[pos + 1][line_num] = ascii[pos + 1][line_num][1:]

            txt[line_num] += ''.join(line)
    return txt

# Test 1999
