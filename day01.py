"""Advent of Code - Day 1"""

from lib.utils import *


def part1(data):
    position = 50
    zeros = 0
    for d in data:
        dir = d[:1]
        steps = int(d[1:])
        if dir == 'L':
            position -= steps
        else:
            position += steps
        if position % 100 == 0:
            zeros += 1
    
    return zeros


def part2(data):
    position = 50
    zeros = 0
    for d in data:
        dir = d[:1]
        steps = int(d[1:])
        for s in range(steps):
            if dir == 'L':
                position -= 1
            else:
                position += 1
            if position % 100 == 0:
                zeros += 1
    
    return zeros
    


if __name__ == "__main__":
    data = read_lines("inputs/day01.txt")
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")
