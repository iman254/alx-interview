#!/usr/bin/python3

"""A script that reads stdin line y line and computes metrics"""
import sys
from collections import defaultdict


def printing_statistics(total_size, status_counts):
    """the function that takes in total_size and status_count as arguments and prints the status """
    print(f"file size: {total_size}")
    for status_code in sorted(status_counts.keys(), key=int):
        if status_code.isdigit():
            print(f"{status_code}: {status_counts[status_code]}")


def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split("")
            if len(parts) != 7:
                continue

            ip, _, _, _, _, status_code, file_size = parts

            if not status_code.isdigit():
                continue

            total_size += int(file_size)
            status_counts[status_code] += 1

            line_count += 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

    if __name__ == "__main__":
        main()
