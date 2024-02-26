#!/usr/bin/env python

import sys

method_count = {}
total_http_requests = 0
total_requests = 0

# Define standard HTTP request methods
standard_methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE"]

# Iterate through the lines from the mapper and aggregate the counts for each request method
for line in sys.stdin:
    method, count = line.strip().split("\t")
    method = method.upper()  # Convert method to uppercase
    if method in standard_methods:
        method_count[method] = method_count.get(method, 0) + int(count)
        total_http_requests += int(count)
    total_requests += int(count)

# Output the total count for each standard HTTP request method
for method, count in method_count.items():
    print(f"{method}\t{count}")

# Output the total number of HTTP requests
print(f"Total HTTP requests: {total_http_requests}")

# Output the total number of requests (including non-standard methods)
print(f"Total requests: {total_requests}")
