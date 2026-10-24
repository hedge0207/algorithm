def max_contiguous_sum(arr):
    local_max = arr[0]
    global_max = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        local_max = max(num, local_max + num)
        if local_max > global_max:
            global_max = local_max

    return global_max