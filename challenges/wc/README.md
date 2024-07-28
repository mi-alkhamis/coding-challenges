
# WC Command-Line Tool

## Overview

This is a Python implementation of the `wc` (word count) command-line utility, designed to display the number of newlines, words, and bytes in a specified file in a format similar to that of the original command.

The main goal of this project is to mimic the behavior of the Linux `wc` command as closely as possible.


Inspired by the Unix `wc` command and the [coding challenges website](https://codingchallenges.fyi/challenges/challenge-wc/).

## Features

- **Print Newline Counts**: Use the `-l` or `--lines` option to print the number of newlines.
- **Print Word Counts**: Use the `-w` or `--words` option to print the number of words.
- **Print Byte Counts**: Use the `-c` or `--bytes` option to print the number of bytes.
- **Print Character Counts**: Use the `-m` or `--chars` option to print the number of characters.
- **Print Maximum Line Length**: Use the `-L` or `--max-line-length` option to print the maximum display width.
- **Print Version Information**: Use the `-v` or `--version` option to print the version information and exit.
- **Handle Input from Files and Pipelines**: Supports reading from a specified file or from the standard input.

## Installation

Clone the repository:

```sh
git clone https://github.com/mi-alkhamis/coding-challenges.git
cd challenges/wc
```

## Usage

Run the tool with a filename:

```sh
python wc.py [OPTIONS] [FILENAME]
```

Or use it with a pipeline:

```sh
cat file.txt | python wc.py [OPTIONS]
```

### Options

- `-l`, `--lines`: Print the newline counts.
- `-w`, `--words`: Print the word counts.
- `-L`, `--max-line-length`: Print the maximum display width.
- `-c`, `--bytes`: Print the byte counts.
- `-m`, `--chars`: Print the character counts.
- `-v`, `--version`: Output version information and exit.

### Examples

Count lines, words, and bytes in a file:

```sh
python wc.py -l -w -c file.txt
```

Count characters and maximum line length from a pipeline:

```sh
cat file.txt | python wc.py -m -L
```

Print version information:

```sh
python wc.py -v
```
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mi-alkhamis/coding-challenges/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Happy coding!
