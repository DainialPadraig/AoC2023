# day1_part2.py
# Description: Day 1, Part 2 of Advent of Code 2020
# Author: Dan Stormont
# Last Modified: 2023-12-02

import re

#input_filename = 'Day1/part2_sample.txt'
input_filename = 'Day1/part1_input.txt'

cal_sum = 0
text_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(input_filename, encoding="utf-8") as f:
    for line in f:
        first_idx = len(line)
        first_num = -1
        left_line = line
        for i in range(0, 9):
            left_idx = line.find(text_num[i])
            if left_idx != -1 and left_idx < first_idx:
                first_idx = left_idx
                first_num = i
        if first_num != -1:
            left_line = left_line.replace(text_num[first_num], str(first_num + 1), 1)
            end_left_line = first_idx + 1
            left_line = left_line[:end_left_line]
        last_idx = 0
        last_num = -1
        right_line = line
        for i in range(0, 9):
            right_idx = line.rfind(text_num[i])
            if right_idx != -1 and right_idx > last_idx:
                last_idx = right_idx
                last_num = i
        if last_num != -1:
            right_line = right_line[:last_idx] + right_line[last_idx:].replace(text_num[last_num], str(last_num + 1), 1)
            right_line = right_line[end_left_line:]
        line = left_line + right_line
        num_list = re.findall(r'\d', line)
        cal_sum += int(num_list[0] + num_list[-1])
    print(cal_sum)  
