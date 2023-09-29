#!/usr/bin/env python3


def print_fibonacci(length):
    if (length == 0):
        print([])
    elif (length == 1):
        print([0])
    else:
        sequence = [0, 1]
        for _ in range(2, length):
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        print(sequence)
