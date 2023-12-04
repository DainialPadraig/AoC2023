# day2_part1.py
# Description: Day 2, Part 1 of Advent of Code 2023
# Author: Dan Stormont
# Last Modified: 2023-12-03

#input_filename = 'Day2/part1_sample.txt'
input_filename = 'Day2/day2_input.txt'

id_sum = 0

with open(input_filename, encoding="utf-8") as f:
    for line in f:
        line = line.replace(":", "")
        line = line.replace(",", "")
        line = line.replace(";", "")
        game_list = line.rstrip('\n').split(" ")
        game_id = game_list[1]
        game_list.pop(0)
        game_list.pop(0)
        game_list = zip(game_list[0::2], game_list[1::2])
        valid_game = True
        for count, color in game_list:
            if int(count) > 14:
                valid_game = False
                break
            elif color == "red" and int(count) > 12:
                valid_game = False
                break
            elif color == "green" and int(count) > 13:
                valid_game = False
                break
        if valid_game:
            id_sum += int(game_id)
    print(id_sum)  
