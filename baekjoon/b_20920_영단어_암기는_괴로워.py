import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words_freq = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if words_freq.get(word):
        words_freq[word] += 1
    else:
        words_freq[word] = 1

sorted_data = sorted(words_freq.items(), key=lambda x:x[1], reverse=True)
freq_words = {}
for word, freq in sorted_data:
    if freq_words.get(freq):
        freq_words[freq].append(word)
    else:
        freq_words[freq] = [word]

for words in freq_words.values():
    words.sort(key=lambda x: (-len(x), x))
    for word in words:
        print(word)
