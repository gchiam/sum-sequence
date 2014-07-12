"""Sequence generator


$ python sum_sequence.py 3
[3]
[2, 1]
[1, 1, 1]

$python sum_sequence.py 6
[6]
[5, 1]
[4, 2]
[4, 1, 1]
[3, 3]
[3, 2, 1]
[3, 1, 1, 1]
[2, 2, 2]
[2, 2, 1, 1]
[2, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
"""

from __future__ import print_function

import argparse


# python 2, 3 compatible
try:
    range = xrange
except NameError:
    pass


def generate_sequence(num):
    assert num > 0
    for element in gen_sub_sequence([num]):
        yield element


def gen_sub_sequence(sequence, previous_first=None):
    first = sequence[0]
    start = first - 1

    if previous_first is None:  # first entry
        yield sequence

    for new_number in range(start, 0, -1):
        second = first - new_number
        new_sequence = [new_number, second] + sequence[1:]
        if new_number >= second:
            yield new_sequence

        new_first = new_sequence[0]
        if len(new_sequence) > 1 and new_sequence[1] > 1:
            sub_sequence = new_sequence[1:]
            sub_first = new_first

            for sub_sequence in gen_sub_sequence(sub_sequence, sub_first):
                if new_first >= sub_sequence[0]:
                    if previous_first is None or previous_first >= new_first:
                        yield [new_first] + sub_sequence


def positive_integer(string):
    msg = '%s is not a positive integer' % string
    try:
        value = int(string)
        if value <= 0:
            raise argparse.ArgumentTypeError(msg)
    except ValueError:
        raise argparse.ArgumentTypeError(msg)
    return value


def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number',
        metavar='N',
        type=positive_integer,
        help='Size (positive integer)')
    args = parser.parse_args()

    for element in generate_sequence(args.number):
        print(element)


if __name__ == '__main__':
    main()
