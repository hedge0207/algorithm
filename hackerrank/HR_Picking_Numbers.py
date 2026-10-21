def pickingNumbers(a):
    num_per_digit = {}
    for digit in a:
        if num_per_digit.get(digit):
            num_per_digit[digit] += 1
        else:
            num_per_digit[digit] = 1

    ans = 0
    for digit, num in num_per_digit.items():
        ans = max(ans, num)
        if digit-1 in num_per_digit:
            ans = max(ans, num + num_per_digit[digit-1])
        if digit+1 in num_per_digit:
            ans = max(ans, num + num_per_digit[digit+1])
    return ans