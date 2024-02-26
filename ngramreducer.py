import sys

current_ngram = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    ngram, count = line.split('\t', 1)
    count = int(count)

    if current_ngram == ngram:
        current_count += count
    else:
        if current_ngram:
            print('%s\t%d' % (current_ngram, current_count))
        current_ngram = ngram
        current_count = count

if current_ngram:
    print('%s\t%d' % (current_ngram, current_count))