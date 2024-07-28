import argparse
import os
import sys

VERSION = '''Code Challenges WC 0.0.1
Author: Milad Alkhamis
Copyright (C) 2024
License: MIT'''


def main():
    parser = argparse.ArgumentParser(description='wc - print newline, word, and byte counts for each file')
    parser.add_argument('filename', type=str, help='gets filename as an argument')
    parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
    parser.add_argument('-L', '--max-line-length', action='store_true', help='print the maximum display width')
    parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
    parser.add_argument('-m', '--chars', action='store_true', help='print the character counts')
    args = parser.parse_args()

    try:
        wc = count(read_file(args.filename))
    except FileNotFoundError:
        print(f'Error: The file {args.filename} was not found.')
        sys.exit(1)
    except IOError as e:
        print(f'Error: An IOError occurred: {e}')
        sys.exit(1)

    if args.lines:
        print(f'    {wc['lines']}', end='   ')
    if args.words:
        print(f'    {wc['words']}', end='   ')
    if args.bytes:
        print(f'    {wc['bytes']}', end='   ')
    if args.chars:
        print(f'    {wc['chars']}', end='   ')
    if args.max_line_length:
        print(f'    {wc['max']}', end='    ')

    if not (args.lines or args.words or args.bytes or args.chars or args.max_line_length):
        print(f'    {wc['lines']}   {wc['words']}  {wc['bytes']}', end='    ')
    print(os.path.split(args.filename)[1])


def count(text):
    lines = text.splitlines()
    words = text.split()
    bytes_count = memoryview(text.encode('utf-8')).nbytes
    chars = len(text)
    max_line_length = calc_max_length(lines)
    return {
        'lines': len(lines),
        'words': len(words),
        'bytes': bytes_count,
        'chars': chars,
        'max': max_line_length,
    }


def calc_max_length(lines):
    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
    return max_length


def read_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as file:
        return file.read()


if __name__ == '__main__':
    main()

