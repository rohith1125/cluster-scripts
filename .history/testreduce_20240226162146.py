#!/usr/bin/env python

import sys

method_count = {}
total_requests = 0

# Iterate through the lines from the mapper and aggregate the counts for each request method
for line in sys.stdin:
    method, count = line.strip().split("\t")
    method_count[method] = method_count.get(method, 0) + int(count)
    total_requests += int(count)

# Output the total count for each request method
for method, count in method_count.items():
    print(f"{method}\t{count}")

# Output the total number of HTTP requests
print(f"Total requests: {total_requests}")
