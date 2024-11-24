def superDigit(n, k):
    if k == 1 and n < 10:
        return n
    return superDigit(k * sum(int(i) for i in str(n)), 1)
