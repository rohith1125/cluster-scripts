import sys

def generate_ngrams(text, n):
    ngrams = []
    for i in range(len(text) - n + 1):
        ngrams.append(text[i:i+n])
    return ngrams

text = sys.stdin.read().strip().lower()

n = int(sys.argv[1])

words = text.split()
for word in words:
    ngrams = generate_ngrams(word, n)
    for ngram in ngrams:
        print('%s\t%d' % (ngram, 1))