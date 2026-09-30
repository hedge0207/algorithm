def move_zeros(lst):
    ans = []
    num_zeros = 0
    for num in lst:
        if num == 0:
            num_zeros += 1
        else:
            ans.append(num)
    return ans + ([0] * num_zeros)