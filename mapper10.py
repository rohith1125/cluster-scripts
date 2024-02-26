import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 6:  
        date = data[3][1:12]  
        status_code = data[8]  
        size = data[9] if data[9] != "-" else "0"  
        print(f"{date}\t{status_code}\t{size}")  

