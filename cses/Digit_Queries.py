def digit_at(k: int) -> str:
    d = 1
    start = 1
    while True:
        block = 9 * start * d
        if k > block:
            k -= block
            d += 1
            start *= 10
        else:
            break

    k -= 1
    idx = k // d
    pos = k % d
    num = start + idx
    print(str(num)[pos])

for _ in range(int(input())):
    digit_at(int(input()))