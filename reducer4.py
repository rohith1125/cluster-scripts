import sys

path_counts = {}

for line in sys.stdin:
    path, count = line.strip().split('\t')
    
    path_counts[path] = path_counts.get(path, 0) + int(count)


most_hit_path = max(path_counts, key=path_counts.get)
total_hits = path_counts[most_hit_path]

print("Most hit path:", most_hit_path)
print("Number of hits:", total_hits)
