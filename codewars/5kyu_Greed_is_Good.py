def score(dice):
    cnt_per_digit = {i: 0 for i in range(1, 7)}
    for digit in dice:
        cnt_per_digit[digit] += 1

    ans = 0
    for digit, cnt in cnt_per_digit.items():
        if digit == 1:
            ans += cnt // 3 * 1000 + cnt % 3 * 100
            continue
        elif digit == 5:
            ans += cnt % 3 * 50
        ans += cnt // 3 * (digit * 100)

    return ans