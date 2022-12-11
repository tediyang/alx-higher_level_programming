#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    # Dicitonary of common roman numerals.
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Create a list where individual characters of the roman
    # strings will be added and the values will be summed to number.
    r_list, number = [], 0

    # Loop through the strings and get their individual characters.
    for r in roman_string:
        # If it is the first character of the string
        # then don't chrck any conditions.
        if not number:
            r_list.append(r)
            number += rom[r]

        # check the last character added to confirm
        # it is a complex roman number (IV, XL etc.) or not.
        else:
            if (r_list[-1] == 'I' and (r == 'V' or r == 'X')) \
             or (r_list[-1] == 'X' and (r == 'L' or r == 'C')) \
             or (r_list[-1] == 'C' and (r == 'D' or r == 'M')):
                number += (rom[r] - rom[r_list[-1]]*2)

            else:
                r_list.append(r)
                number += rom[r]

    return number
