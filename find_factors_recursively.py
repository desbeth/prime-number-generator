"""
File Name: find_factors_recursively.py
Author: desbeth || Claire
Purpose: Until the recursive limit is reached, this will iterate through a list and find all the prime numbers.
"""


# parameters:       list       int
def find_factors(old_list, user_input):
    i = 0
    length = len(old_list)
    while True:
        if (user_input % old_list[i]) != 0:
            if (i + 1) == length:
                old_list.append(user_input)
                print(old_list)
                find_factors(old_list, user_input + 1)
            else:
                i += 1
        else:
            find_factors(old_list, user_input + 1)
