import sys

status_404_count = 0

for line in sys.stdin:
    status_code, count = line.strip().split('\t')  
    if status_code == "404":  
        status_404_count += int(count)  

print("Total number of requests with status code 404:", status_404_count)

