def migratoryBirds(arr):
    cnt = {}
    for bird in arr:
        if bird in cnt:
            cnt[bird] += 1
        else:
            cnt[bird] = 1

    ans = 0
    max_bird = 0
    for id_, num in cnt.items():
        if num > max_bird or (num == max_bird and ans > id_):
            ans = id_
            max_bird = num
    return ans