def f(A, B):
    if B % 2 == 1:
        return f(A, B - 1) * A
    elif B == 0:
        return 1
    elif B == 1:
        return A
    else:
        ans = f(A, B//2)
        return ans ** 2 % C

A, B, C = map(int, input().split())

print(f(A, B) % C)