#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.parser import parse_arguments


def main():
    args = parse_arguments()
    diff = generate_diff(args.file_path_1, args.file_path_2, args.format)
    print(diff)


if __name__ == '__main__':
    main()
