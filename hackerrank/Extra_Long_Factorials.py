def extraLongFactorials(n, is_first=True):
    if n == 1:
        if is_first:
            print(1)
        return 1
    result = n * extraLongFactorials(n-1, False)
    if is_first:
        print(result)
    return result
