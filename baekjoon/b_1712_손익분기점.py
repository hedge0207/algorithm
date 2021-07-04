A, B, C = list(map(int, input().split(' ')))


def calculate_break_even_point(a, b, c):
    benefit = c - b
    if benefit <= 0:
        print(-1)
        return

    print(a // benefit + 1)


calculate_break_even_point(A, B, C)
