import sys

request_counts = {}
total_requests = 0
standard_methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE"]

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        if data[0].endswith("_count"):
            total_requests += int(data[1])
        else:
            request_counts[data[0]] = request_counts.get(data[0], 0) + int(data[1])

# Compute total count for standard request methods
total_standard_requests = sum(request_counts[method] for method in standard_methods)

for method, count in request_counts.items():
    print(method, count, sep='\t')

print("Total_HTTP_requests", total_requests, sep='\t')
print("Total_Standard_HTTP_requests", total_standard_requests, sep='\t')
