import sys

request_counts = {}
total_requests = 0
standard_methods = ['\"GET', '\"POST', '\"HEAD', '\"PUT', '\"DELETE', '\"OPTIONS', '\"TRACE']
standard_requests_total = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        if data[0].endswith("_count"):
            total_requests += int(data[1])
            if data[0].rstrip("_count") in standard_methods:
                standard_requests_total += int(data[1])
        else:
            request_counts[data[0]] = request_counts.get(data[0], 0) + int(data[1])

for method, count in request_counts.items():
    print(method, count, sep='\t')

print("Total requests", total_requests, sep='\t')
print("Total_standard_HTTP_requests", standard_requests_total, sep='\t')
