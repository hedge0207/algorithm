def strangeCounter(t):
    num = 3
    sum_ = 3
    while sum_ < t:
        num *= 2
        sum_ += num
    return num - (t - (sum_-num)) + 1