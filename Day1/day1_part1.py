# day1_part1.py
# Description: Day 1, Part 1 of Advent of Code 2020
# Author: Dan Stormont
# Last Modified: 2023-12-01

import re

#input_filename = 'Day1/part1_sample.txt'
input_filename = 'Day1/part1_input.txt'

cal_sum = 0

with open(input_filename, encoding="utf-8") as f:
    for line in f:
        num_list = re.findall(r'\d', line)
        cal_sum += int(num_list[0] + num_list[-1])
    print(cal_sum)  
