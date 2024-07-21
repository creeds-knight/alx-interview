#!/usr/bin/python3
"""
    A Script to parse logs from stdin and return formatted output
"""
import sys
import re
import signal

total_file_size = 0
list_of_codes = [200, 301, 499, 401, 403, 404, 405, 500]
status_codes = {code: 0 for code in list_of_codes}
line_count = 0

pattern = re.compile(
    r'\s*(?P<ip>\S+)\s*'
    r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]'
    r'\s*"(?P<request>[^"]*)"\s*'
    r'\s*(?P<status_code>\d+)\s*'
    r'\s*(?P<file_size>\d+)'
)


def print_stats():
    """ Prints the output to the screen """
    global total_file_size
    global status_codes

    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}:{status_codes[code]}")


def signal_handler(signal, frame):
    """ Handle Keyboard interrupt Ctrl+c """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


try:
    for line in sys.stdin:
        parts = line.split()
        protocol = parts[6][:-1]
        status_code = parts[7]
        file_size = parts[8]
        # print(protocol, status_code, file_size)

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1
        total_file_size += file_size

        line_count += 1

        if line_count % 10 == 0:
            print_stats()
except Exception as e:
    print(str(e))
