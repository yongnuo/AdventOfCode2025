"""Advent of Code - Day 3"""

from lib.utils import *


def part1(data):
    total = 0
    for line in data:
        max1 = max(line[:-1])
        index1 = line.index(max1)
        max2 = max(line[index1+1:])
        jolt = int(line[index1] + max2)
        total += jolt

    return total


def part2(data):
    total = 0
    for line in data:
        range_max = len(line) - 12
        local_max = 0
        for i in range(0, range_max):
            val = int(line[i:i+12])
            if val > local_max:
                local_max = val
        total += local_max
        
    return total


if __name__ == "__main__":
    data = read_lines("inputs/day03.txt")
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")
