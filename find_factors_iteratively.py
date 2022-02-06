"""
File Name: find_factors_iteratively.py
Author: desbeth || Claire
Purpose: Until the recursive limit is reached, this will iterate through a list and find all the prime numbers.
"""


# parameters:       list       int
def find_factors(old_list, user_input):
    i = 0
    while True:
        length = len(old_list)
        if (user_input % old_list[i]) != 0:
            if (i + 1) == length:
                old_list.append(user_input)
                print(old_list)
                user_input += 1
                i = 0
            else:
                i += 1
        else:
            user_input += 1
            i = 0
