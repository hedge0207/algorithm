def is_square(n):
    if n < 0:
        return False
    if n * n == n:
        return True
    for i in range(n):
        if i * i == n:
            return True
        elif i * i > n:
            return False


print(is_square(25))


# best_practice
def is_square(n):
    return n >= 0 and (n ** 0.5) % 1 == 0
