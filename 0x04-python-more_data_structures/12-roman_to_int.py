#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':5
            0, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(roman_string)):
        current = roman_dict[roman_string[i]]
        if i < len(roman_string) - 1 and
        roman_dict[roman_string[i+1]] > current:
            result -= current
        else:
            result += current
        return result
