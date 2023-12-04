# day2_part2.py
# Description: Day 2, Part 2 of Advent of Code 2023
# Author: Dan Stormont
# Last Modified: 2023-12-03

#input_filename = 'Day2/part1_sample.txt'
input_filename = 'Day2/day2_input.txt'

power_sum = 0

with open(input_filename, encoding="utf-8") as f:
    for line in f:
        line = line.replace(":", "")
        line = line.replace(",", "")
        line = line.replace(";", "")
        game_list = line.rstrip('\n').split(" ")
        game_list.pop(0)
        game_list.pop(0)
        game_list = zip(game_list[0::2], game_list[1::2])
        max_colors = [0, 0, 0]
        for count, color in game_list:
            if color == "red":
                if int(count) > max_colors[0]:
                    max_colors[0] = int(count)
            elif color == "green":
                if int(count) > max_colors[1]:
                    max_colors[1] = int(count)
            elif color == "blue":
                if int(count) > max_colors[2]:
                    max_colors[2] = int(count)
        power_sum += max_colors[0] * max_colors[1] * max_colors[2]
    print(power_sum)  
