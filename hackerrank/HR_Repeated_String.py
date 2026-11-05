def repeatedString(s, n):
    length = len(s)
    prefix_num_a = [0] * (length + 1)
    num_a = 0
    for i in range(length):
        char = s[i]
        if char == "a":
            num_a += 1
        prefix_num_a[i+1] = num_a

    return (n // length * prefix_num_a[-1]) + (prefix_num_a[n % length])