import sys

ip_counts = {}

for line in sys.stdin:
    ip_address, count = line.strip().split('\t')
    
    ip_counts[ip_address] = ip_counts.get(ip_address, 0) + int(count)

most_accessed_ip = max(ip_counts, key=ip_counts.get)
total_accesses = ip_counts[most_accessed_ip]

print("Most accessed IP:", most_accessed_ip)
print("Number of accesses:", total_accesses)
