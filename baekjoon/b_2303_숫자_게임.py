NUM_CARDS = 3
def find_biggest_num(st, d, sum_):
    global max_num
    if d == 3:
        max_num = max(max_num, sum_%10)
        return

    for i in range(st, len(cards)):
        find_biggest_num(i+1, d+1, sum_+cards[i])

n = int(input())
winner = 0
max_val = -1
for i in range(1, n+1):
    max_num = 0
    cards = list(map(int, input().split()))
    find_biggest_num(0, 0, 0)
    if max_num >= max_val:
        winner = i
        max_val = max_num
print(winner)