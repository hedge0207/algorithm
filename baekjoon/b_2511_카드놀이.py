cards_a = list(map(int, input().split()))
cards_b = list(map(int, input().split()))

score_a = 0
score_b = 0
last_winner = ""
for i in range(10):
    if cards_a[i] == cards_b[i]:
        score_a += 1
        score_b += 1
    else:
        if cards_a[i] > cards_b[i]:
            score_a += 3
            last_winner = "A"
        else:
            score_b += 3
            last_winner = "B"

print(score_a, score_b)
if score_a == score_b:
    if score_a == 10:
        print("D")
    else:
        print(last_winner)
elif score_a > score_b:
    print("A")
else:
    print("B")


