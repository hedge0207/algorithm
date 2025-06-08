def isValid(s):
    chars = sorted(list(s))
    nums = []
    cnt = 1
    for i in range(1, len(chars)):
        if chars[i] != chars[i-1]:
            nums.append(cnt)
            cnt = 1
        else:
            cnt += 1
    nums.append(cnt)

    cnt_per_nums = {}
    max_cnt = 0
    most_freq_num = 0
    for num in nums:
        if cnt_per_nums.get(num):
            cnt_per_nums[num] += 1
        else:
            cnt_per_nums[num] = 1
        if max_cnt < cnt_per_nums[num]:
            max_cnt = cnt_per_nums[num]
            most_freq_num = num

    removed = False
    for num in nums:
        if num != most_freq_num:
            if not removed and (num-1 == most_freq_num or num-1 == 0):
                removed = True
                continue
            return "NO"
    return "YES"