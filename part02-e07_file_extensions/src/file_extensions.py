#!/usr/bin/env python3

from collections import defaultdict


def file_extensions(filename):
    no_ext = []
    files_by_ext = defaultdict(list)
    with open(filename) as f:
        for line in f:
            file = line.strip()
            dot_pos = file.rfind(".")
            if dot_pos == -1:
                no_ext.append(file)
            else:
                ext = file[dot_pos + 1 :]
                files_by_ext[ext].append(file)

    return (no_ext, files_by_ext)


def main():
    no_ext, files_by_ext = file_extensions("src/filenames.txt")
    print(f"{len(no_ext)} files with no extension")
    for ext in sorted(files_by_ext.keys()):
        print(f"{ext} {len(files_by_ext[ext])}")


if __name__ == "__main__":
    main()
