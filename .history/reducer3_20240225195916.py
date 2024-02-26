import sys

request_counts = {}
total_requests = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 2:
        if data[0].endswith("_count"):
            total_requests += int(data[1])
        else:
            request_counts[data[0]] = request_counts.get(data[0], 0) + int(data[1])

for method, count in request_counts.items():
    print(method, count, sep='\t')

print("Total_HTTP_requests", total_requests, sep='\t')
