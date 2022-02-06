"""
File Name: main.py for primeNumberCalculator
Author: desbeth || Claire
Purpose: This is the user interface with the terminal.
"""
import threading

import find_factors_iteratively
import find_factors_recursively
import find_factors_from_input
import int_in_list_counter
import prime_file
import sys


prime_number_list = prime_file.get_prime_list()


def main():
    # generates an "infinite" loop printing out lists of prime numbers from the last number in the list iteratively
    # HIGHLY RECOMMENDED!
    # find_factors_iteratively.find_factors(prime_number_list, 1003337)
    # generates an "infinite" loop printing out lists of prime numbers from the last number in the list recursively
    # NOT RECOMMENDED BUT STILL AN OPTION!
    #find_factors_recursively.find_factors(prime_number_list, 1003337)

    # the actual user interface
    user_input = input("Input a number to find out its factors (1-1,000,000): ")
    getter_list = find_factors_from_input.find_factors_in_input(prime_number_list, [], int(user_input))
    print(int_in_list_counter.counter(getter_list))



if __name__ == "__main__":
    recurs_limit = 2 ** 30
    sys.setrecursionlimit(recurs_limit)
    threading.stack_size(0x2000000)
    thread = threading.Thread(target=main())
    thread.start()
