def is_all_same_color() -> bool:
    pre_col = cards[0][0]
    for i in range(1, n):
        color, num = cards[i]
        if color != pre_col:
            return False
        pre_col = color
    return True

def is_consecutive() -> bool:
    pre_card = cards[0][1]
    for i in range(1, n):
        if cards[i][1] - 1 != pre_card:
            return False
        pre_card = cards[i][1]
    return True

def calculate_bonus_by_num() -> int:
    count = {}
    for card in cards:
        num = card[1]
        if count.get(num):
            count[num] += 1
        else:
            count[num] = 1
    three_num = -1
    two_num = -1
    for num, value in count.items():
        if value == 4:
            return num + 800
        if value == 3:
            three_num = num
        if value == 2:
            if two_num != -1:
                max_two_num, min_two_num = max(num, two_num), min(num, two_num)
                return max_two_num*10+min_two_num+300
            two_num = num
        if three_num != -1 and two_num != -1:
            return three_num * 10 + two_num + 700

    if three_num != -1:
        return three_num + 400

    if two_num != -1:
        return two_num + 200
    return 0


def calculate_score():
    score = 0
    if is_all_same_color() and is_consecutive():
        return cards[-1][1] + 900
    if is_all_same_color():
        return max(cards[-1][1] + 600, calculate_bonus_by_num())
    if is_consecutive():
        return cards[-1][1] + 500
    score += calculate_bonus_by_num()
    if score == 0:
        score += cards[-1][1] + 100
    return score

n = 5
cards = sorted(list(map(lambda x:[x[0], int(x[1])],[input().split() for _ in range(n)])), key=lambda x:x[1])
print(calculate_score())