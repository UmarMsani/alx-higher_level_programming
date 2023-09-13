#!/usr/bin/python3


import sys

def compute_metrics(lines):
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in lines:
        parts = line.split()
        if len(parts) >= 9:
            status_code = int(parts[8])
            file_size = int(parts[9])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

    return total_size, status_counts

def print_metrics(total_size, status_counts):
    print("Total file size:", total_size)
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))

lines = []
try:
    for line in sys.stdin:
        lines.append(line)
        if len(lines) == 10:
            total_size, status_counts = compute_metrics(lines)
            print_metrics(total_size, status_counts)
            lines = []
except KeyboardInterrupt:
    total_size, status_counts = compute_metrics(lines)
    print_metrics(total_size, status_counts)
