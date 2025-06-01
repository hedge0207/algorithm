def biggerIsGreater(w):
    chars = list(w)
    n = len(w)

    for i in range(n-1, 0, -1):
        if chars[i] > chars[i-1]:
            idx_to_change = i
            break
    else:
        return "no answer"

    min_greater_char_idx = idx_to_change
    for j in range(n-1, idx_to_change, -1):
        if chars[idx_to_change - 1] < chars[j]:
            min_greater_char_idx = j
            break

    chars[idx_to_change-1], chars[min_greater_char_idx] = chars[min_greater_char_idx], chars[idx_to_change-1]
    return "".join(chars[:idx_to_change] + sorted(chars[idx_to_change:]))





print(biggerIsGreater("dcba"))
"hcdk"