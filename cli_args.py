# Accepting Arguments
# Simple example using `sys` library, but not secure or efficient
# import sys

# name = sys.argv[1]
# print(f"Hello {name}!")
# Using `argparse`, another standard library
import argparse

parser = argparse.ArgumentParser(
    description="This program prints the name of my cats"
)

parser.add_argument("-c", "--color", metavar="color",
                    required=True, choices={"red", "black"}, help="the color to search for")

args = parser.parse_args()

print(args.color)
