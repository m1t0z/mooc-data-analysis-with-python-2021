#!/usr/bin/env python3

import sys


def file_count(filename):
    with open(filename) as f:
        linecount = 0
        wordcount = 0
        charactercount = 0
        for line in f:
            linecount += 1
            wordcount += len(line.split())
            charactercount += len(line)

        return linecount, wordcount, charactercount


def main():
    for filename in sys.argv[1:]:
        cnt_lines, cnt_words, cnt_characters = file_count(filename)
        print(f"{cnt_lines}\t{cnt_words}\t{cnt_characters}\t{filename}")


if __name__ == "__main__":
    main()
