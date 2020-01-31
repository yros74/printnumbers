#!/usr/bin/env python3
import random
numbers = list(range(1,11))  # create a list with numbers 1 to 10
random.shuffle(numbers)  # shuffle the list
print(*numbers) # print the numbers without brackets
# if you want to print the numbers in line  you can write
# print(*numbers, sep = "\n")  # this will print each number in  separate line

