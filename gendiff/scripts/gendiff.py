#!/usr/bin/env python

import argparse
from gendiff import generate_diff


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration\
    files and shows a difference.')

    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    parser.add_argument('first_file', help='first file to compare')
    parser.add_argument('second_file', help='second file to compare')

    args = parser.parse_args()

    if args.format == 'stylish':
        print(generate_diff(args.first_file, args.second_file))
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, 'plain'))
    if args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, 'json'))


if __name__ == '__main__':
    main()
