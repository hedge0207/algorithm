def appendAndDelete(s, t, k):
    if s == t:
        return "Yes"

    n, m = len(s), len(t)
    if n + m <= k:
        return "Yes"
    diff_idx = -1
    i = 0
    while i < n and i < m:
        if s[i] != t[i]:
            diff_idx = i
            break
        i += 1

    if diff_idx == -1:
        if abs(n-m) > k:
            return "No"
        if abs(n-m) == k or (k - abs(n-m)) % 2 == 0:
            return "Yes"

    num_operation = n - diff_idx
    num_operation += m - diff_idx
    if num_operation <= k:
        return "Yes"

    return "No"