#!/usr/bin/env python3

import generate_embed
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    else:
        directory = input ("Directory to Scan: ")
    generate_embed.my_main(directory)