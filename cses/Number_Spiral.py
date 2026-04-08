for _ in range(int(input())):
    r, c = map(int, input().split())
    line = max(r, c)

    ans = 1 + (line-1)**2
    if line % 2 == 0:
        ans += r-1
        if line != c:
            ans += line-c
    else:
        ans += c - 1
        if line != r:
            ans += line-r
    print(ans)