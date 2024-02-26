import sys

requested_data = 0

target_date = "19/Dec/2020"

for line in sys.stdin:
    date, size = line.strip().split('\t')  
    if date == target_date:  
        requested_data += int(size) 

print(f"Total data requested on {target_date}: {requested_data} bytes")

