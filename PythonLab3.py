import argparse
import numpy
import os
import math

def main(number: int) -> int:
    list_factors = []
    while number >= 0:
        list_factors.append(number)
        number-=1
    cubed_list = [i**3 for i in list_factors]
    copy_cubed_list = cubed_list.copy()
    keep_list = []
    for element in copy_cubed_list:
        trial_element = element
        while trial_element >= 10:
            trial_element = trial_element // 10
        if trial_element % 2 == 0:
            keep_list.append(element)
    sum_of_list = sum(keep_list)
    print(sum_of_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)

