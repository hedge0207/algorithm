def f(n, r, c):
    if n == 1:
        return

    sr = r + n // 3
    er = r + n // 3 * 2
    sc = c + n // 3
    ec = c + n // 3 * 2
    for i in range(sr, er):
        for j in range(sc, ec):
            stars[i][j] = ' '

    f(n // 3, r, c)
    f(n // 3, sr, c)
    f(n // 3, er, c)
    f(n // 3, r, sc)
    f(n // 3, r, ec)
    f(n // 3, sr, ec)
    f(n // 3, er, sc)
    f(n // 3, er, ec)
    #sr,sc는 굳이 할 필요 없다.

N = int(input())
stars = [['*'] * N for _ in range(N)]
f(N, 0, 0)
for i in range(N):
    for j in range(N):
        print(stars[i][j], end="")
    print()

#https://suri78.tistory.com/141참조
