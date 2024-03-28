#!/usr/bin/python3
import sys
import re
from signal import signal, SIGINT

# Initialize variables
total_size = 0
status_code_counts = {}
line_count = 0

def handler(signal_received, frame):
    # Print statistics upon receiving a SIGINT (CTRL+C)
    print_statistics()
    sys.exit(0)

def print_statistics():
    print("Total file size: File size: {}".format(total_size))
    for status_code in sorted(status_code_counts.keys()):
        print("{}: {}".format(status_code, status_code_counts[status_code]))

# Regular expression to match the log line format
log_line_format = re.compile(r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)')

# Handle SIGINT (CTRL+C) to print statistics before exiting
signal(SIGINT, handler)

try:
    for line in sys.stdin:
        # Match the line with the specified format
        match = log_line_format.match(line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update total file size and status code counts
            total_size += file_size
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()
except KeyboardInterrupt:
    # Print statistics if interrupted
    print_statistics()
finally:
    # Also print statistics if the script ends normally
    if line_count > 0:
        print_statistics()

