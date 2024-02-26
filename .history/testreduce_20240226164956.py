#!/usr/bin/env python

import sys

method_count = {}
total_http_requests = 0
total_requests = 0

# Iterate through the lines from the mapper and aggregate the counts for each request method
for line in sys.stdin:
    method, count = line.strip().split("\t")
    method = method.lower()  # Convert method to lowercase
    if method in ["get", "post", "head", "put", "delete", "options", "trace"]:
        method_count[method] = method_count.get(method, 0) + int(count)
        total_http_requests += int(count)
    total_requests += int(count)

# Output the total count for each request method
for method, count in method_count.items():
    print(f"{method}\t{count}")

# Output the total number of HTTP requests
print(f"Total HTTP requests: {total_http_requests}")

# Output the total number of requests (including non-standard methods)
print(f"Total requests: {total_requests}")
