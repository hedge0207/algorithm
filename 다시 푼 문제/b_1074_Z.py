def search(n, r, c):
    if n == 0:
        return 0

    half = 2**(n-1)
    if r < half and c < half:
        return search(n - 1, r, c)
    elif r < half <= c:
        return half**2 * 1 + search(n - 1, r, c - half)
    elif r >= half > c:
        return half**2 * 2 + search(n - 1, r - half, c)
    else:
        return half**2 * 3 + search(n - 1, r - half, c - half)


n, r, c = map(int, input().split())
print(search(n, r, c))
