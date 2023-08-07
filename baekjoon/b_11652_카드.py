from collections import defaultdict
import sys


input = sys.stdin.readline
N = int(input())
cards = defaultdict(int)
for _ in range(N):
    cards[int(input())] += 1

result = 0
max_num = -1
for card, num in cards.items():
    if num == max_num:
        if card < result:
            result = card
    elif num > max_num:
        result = card
        max_num = num

print(result)