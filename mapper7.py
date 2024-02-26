import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 8:  
        status_code = data[8]  
        print(status_code + "\t1")  

