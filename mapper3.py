import sys

request_counts = {}

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = " ".join(data[5:-2])  
        request_method = request_line.split()[0]
        request_counts[request_method] = request_counts.get(request_method, 0) + 1
        print(request_method + "\t1")

for method, count in request_counts.items():
    print(method + "_count" + "\t" + str(count))
