import sys
target_ip = "96.32.128.5"
for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 0:
        ip_address = data[0]
        if ip_address == target_ip:
            print(ip_address + "\t1")
