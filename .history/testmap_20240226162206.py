#!/usr/bin/env python

import sys

# Iterate through the lines in the log file and emit the request method with count 1
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) > 5:
        method = data[5].replace('"', '')  # Extracting the request method
        print(f"{method}\t1")
