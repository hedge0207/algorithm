def pairs(k, arr):
    arr.sort()
    st = 0
    ans = 0
    for ed in range(1, len(arr)):
        while st < ed and arr[ed] - arr[st] >= k:
            if arr[ed] - arr[st] == k:
                ans += 1
            st += 1
    return ans