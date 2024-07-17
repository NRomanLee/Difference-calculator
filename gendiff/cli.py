#!/usr/bin/env python3
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="Path to the first configuration file")
    parser.add_argument("second_file", help="Path to the second configuration file")
    parser.add_argument('-f', '--format', help='Set format of output', default='stylish',
                        choices=['stylish', 'plain', 'json'])
    return parser.parse_args()

def main():
    args = parse_args()
    print(args)

if __name__ == "__main__":
    args = parse_args()
    print(args)
