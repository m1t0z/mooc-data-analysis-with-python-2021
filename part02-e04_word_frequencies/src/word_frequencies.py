#!/usr/bin/env python3
from collections import Counter


def word_frequencies(filename):
    with open(filename) as f:
        words = map(lambda w: w.strip("""!"#$%&'()*,-./:;?@[]_"""), f.read().split())
        return Counter(words)


def main():
    for word, counter in word_frequencies("src/alice.txt").items():
        print(f"{word}\t{counter}")


if __name__ == "__main__":
    main()
