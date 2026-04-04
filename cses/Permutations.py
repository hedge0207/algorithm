def make_beautiful_permutation(n):
    if 1 < n < 4:
        print("NO SOLUTION")
        return
    odd, even = [], []
    for i in range(1, n+1):
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    print(" ".join(map(str, even + odd)))

make_beautiful_permutation(int(input()))