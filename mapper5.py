import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 0:
        ip_address = data[0]
        print(ip_address + "\t1")

