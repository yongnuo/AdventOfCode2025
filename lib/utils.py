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
