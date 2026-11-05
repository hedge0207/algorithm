def plusMinus(arr):
    n = len(arr)
    pos, neg, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    print(f"{pos / n:.6f}")
    print(f"{neg / n:.6f}")
    print(f"{zero / n:.6f}")