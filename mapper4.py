import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = " ".join(data[5:-2])
        request_parts = request_line.split()
        if len(request_parts) > 1:
            path = request_parts[1]
            print(path + "\t1")

