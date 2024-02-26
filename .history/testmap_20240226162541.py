#!/usr/bin/env python

import sys

# Define the function to parse the log and emit the request method
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) > 5:
        method = data[5].split('"')[1].split()[0]  # Extracting the request method
        print(f"{method}\t1")  # Emit the request method with count 1
