import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) > 5:
        request_line = data[5]  
        if request_line == "\"POST":
            print("POST" + "\t1")

