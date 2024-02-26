import sys

ip_data = {}


for line in sys.stdin:
    
    ip, size = line.strip().split('\t')
    size = int(size)
    # Update the total 
    if ip in ip_data:
        ip_data[ip] += size
    else:
        ip_data[ip] = size

sorted_ips = sorted(ip_data.items(), key=lambda x: x[1], reverse=True)


for ip, total_size in sorted_ips[:3]:
    print(f"{ip}\t{total_size}")

