num = input()
digits = {str(i):0 for i in range(9)}
for digit in num:
    if digit == "9":
        digit = "6"
    digits[digit] += 1

ans = 0
for digit, cnt in digits.items():
    if digit == "6":
        if cnt % 2:
            cnt = cnt // 2 + 1
        else:
            cnt //= 2
    ans = max(ans, cnt)
print(ans)