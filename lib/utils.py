"""Utility functions for Advent of Code solutions."""


def read_input(filename):
    """Read input file and return contents as string."""
    with open(filename, 'r') as f:
        return f.read()


def read_lines(filename):
    """Read input file and return list of lines."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def read_integers(filename):
    """Read input file and return list of integers."""
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]

def chunkstring(string, length):
    return [string[0+i:length+i] for i in range(0, len(string), length)]

def all_same(items):
    return all(x == items[0] for x in items)