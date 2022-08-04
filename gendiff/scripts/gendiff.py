#!/usr/bin/env python


import argparse


def main():
    
    parser = argparse.ArgumentParser(description = 'Compares two configuration files and shows a difference.')

    parser.add_argument("first_file", help = 'first file to compare')
    parser.add_argument("second_file", help = 'second file to compare')

    args = parser.parse_args()


if __name__ == '__main__':
    main()