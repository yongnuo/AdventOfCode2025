"""Advent of Code - Day 2"""

from lib.utils import read_input, chunkstring, all_same


def part1(data):
    total = 0
    parts = [d.strip() for d in data.strip().split(",")]
    """Solve part 1."""
    for part in parts:
        spl = part.split("-")
        fr = int(spl[0])
        to = int(spl[1])
        for n in range(fr, to + 1):
            n_as_string = str(n)
            l = len(n_as_string)
            if l % 2 == 1:
                # print("Odd length: " + n_as_string)
                continue
            if n_as_string[:(l//2)] == n_as_string[(l//2):]:
                total += n

    return total

def part2(data):
    total = 0
    parts = [d.strip() for d in data.strip().split(",")]
    for part in parts:
        spl = part.split("-")
        fr = int(spl[0])
        to = int(spl[1])
        for n in range(fr, to + 1):
            n_as_string = str(n)
            l = len(n_as_string)
            found = False
            for i in range(1, l+1):
                if not found and i != 1 and l % i == 0:
                    chunks = chunkstring(n_as_string, l // i)
                    if all_same(chunks):
                        found = True
            if found:
                total += n
                        

    return total

if __name__ == "__main__":
    data = read_input("inputs/day02.txt")
    
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    result2 = part2(data)
    print(f"Part 2: {result2}")
