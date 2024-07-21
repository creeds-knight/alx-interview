#!/usr/bin/python3
"""
    A Script to parse logs from stdin and return formatted output
"""
import sys
import signal

total_file_size = 0
list_of_codes = [200, 301, 499, 401, 403, 404, 405, 500]
status_codes = {str(code): 0 for code in list_of_codes}
line_count = 0


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


def run():
    """ Main entry point to program """

    global total_file_size
    global status_codes
    global line_count

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            status_code = parts[7]
            file_size = parts[8]

            try:
                status_code = str(status_code)
                file_size = int(file_size)
            except ValueError:
                continue

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_file_size += file_size

            line_count += 1

            if line_count % 10 == 0:
                print_stats()
        print_stats()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    run()
