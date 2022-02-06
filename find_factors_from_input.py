"""
File Name: find_factors_from_input.py
Author: desbeth || Claire
Purpose: This creates a list which has how many times a prime number is found in a number.
"""


# parameters                list       list          int
def find_factors_in_input(old_list, output_list, user_input):
    i = 0
    length = len(old_list)
    while True:
        if (user_input % old_list[i]) != 0:
            if (i + 1) == length:
                old_list.append(user_input)
                output_list.sort()
                return output_list
            else:
                i += 1
        else:
            list_getter = old_list[i]
            getter_result = user_input / list_getter
            output_list.append(list_getter)
            return find_factors_in_input(old_list, output_list, getter_result)
