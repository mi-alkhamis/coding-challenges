import argparse
import os
import sys

VERSION = '''
    Code Challenges WC 0.0.1
    MIT License
    Copyright (c) 2024
    '''


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.version:
        print_version()
        sys.exit(0)

    if sys.stdin.isatty():
        if not args.filename:
            print("Error: No input provided. Please specify a filename or pipe input.")
            sys.exit(1)
        try:
            text = read_file(args.filename)
        except FileNotFoundError:
            print(f'Error: The file {args.filename} was not found.')
            sys.exit(1)
        except IOError as e:
            print(f'Error: An IOError occurred: {e}')
            sys.exit(1)
    else:
        text = sys.stdin.read()

    wc = count(text)
    display_results(wc, args)


def display_results(wc, args):
    output = []
    if args.lines:
        output.append(f'{wc['lines']}')
    if args.words:
        output.append(f'{wc['words']}')
    if args.bytes:
        output.append(f'{wc['bytes']}')
    if args.chars:
        output.append(f'{wc['chars']}')
    if args.max_line_length:
        output.append(f'{wc['max']}')
    if not (args.lines or args.words or args.bytes or args.chars or args.max_line_length):
        output.append(f'{wc["lines"]}   {wc["words"]}  {wc["bytes"]}')
    if sys.stdin.isatty():
        output.append(os.path.split(args.filename)[1])
    print(' '.join(output))


def create_parser():
    parser = argparse.ArgumentParser(description='wc - print newline, word, and byte counts for each file')
    parser.add_argument('filename', type=str, nargs='?', help='gets filename as an argument')
    parser.add_argument('-l', '--lines', action='store_true', help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
    parser.add_argument('-L', '--max-line-length', action='store_true', help='print the maximum display width')
    parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
    parser.add_argument('-m', '--chars', action='store_true', help='print the character counts')
    parser.add_argument('-v', '--version', action='store_true', help='output version information and exit')
    return parser


def print_version():
    print(VERSION)


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
