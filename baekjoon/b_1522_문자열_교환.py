def replace_char(input_string: str):
    num_b = 0
    for char in input_string:
        if char == "b":
            num_b += 1
    if num_b == 0:
        return 0

    ans = float("inf")
    num_b_in_window = 0
    for i in range(num_b):
        if input_string[i] == "b":
            num_b_in_window += 1
    for i in range(num_b, len(input_string) + num_b):
        if i >= len(input_string):
            i %= len(input_string)
        ans = min(ans, num_b - num_b_in_window)
        if input_string[i] == "b":
            num_b_in_window += 1
        if input_string[i-num_b] == "b":
            num_b_in_window -= 1
    ans = min(ans, num_b - num_b_in_window)
    return ans

print(replace_char(input()))
