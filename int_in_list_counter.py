"""
File Name: int_in_list_counter.py
Author: desbeth || Claire
Purpose: Takes a list of ints and returns how many times they are used, ex.: [3, 3] would return 3^2
"""


# parameters:  list
def counter(old_list):
    old_list.sort()
    incrementer = 1
    length = len(old_list)
    starting_int = old_list[0]
    count = 1
    while True:
        if incrementer == length:
            return str(starting_int) + "^" + str(count)
        elif old_list[incrementer] == starting_int:
            count += 1
            incrementer += 1
        else:
            old_list = old_list[incrementer:]
            return (str(starting_int) + "^" + str(count)) + "," + counter(old_list)
