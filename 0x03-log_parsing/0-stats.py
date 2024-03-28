#!/usr/bin/python3
"""
<<<<<<< HEAD
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
=======
log parsing
"""

import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if (match):
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # status code
                if (code.isdecimal()):
                    log["code_frequency"][code] += 1

                if (line_count % 10 == 0):
                    output(log)
    finally:
        output(log)
>>>>>>> c6ba8cd662b9223ac61e33ba6f7d266a22b3303f
