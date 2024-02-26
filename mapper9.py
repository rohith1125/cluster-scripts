import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) >= 10:
        ip = data[0]
        size = data[9]
        if size != '-':
            size = int(size)
            print(f"{ip}\t{size}")

