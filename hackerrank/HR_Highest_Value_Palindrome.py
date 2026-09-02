def highestValuePalindrome(s, n, k):
    changed = set()
    half = n//2 + 1 if n % 2 else n//2
    digits = list(map(int, s))
    for st in range(half):
        ed = n-st-1
        if digits[st] == digits[ed]:
            continue

        if digits[st] > digits[ed]:
            digits[ed] = digits[st]
        elif digits[ed] > digits[st]:
            digits[st] = digits[ed]
        changed.add(st)
        k -= 1

    if k < 0:
        return "-1"

    st = 0
    while k > 0 and st < half:
        ed = n-st-1
        if digits[st] != 9:
            required = 2
            if st in changed:
                required -= 1
            if st == ed:
                required = 1
            if required <= k:
                digits[st], digits[ed] = 9, 9
                k -= required
        st += 1
    return "".join(map(str,digits))