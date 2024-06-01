def backtrack(d, indices):
    if d == k:
        combination.add("".join([cards[idx] for idx in indices]))
        return

    for i in range(n):
        if i in indices:
            continue
        backtrack(d + 1, indices + [i])


n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
combination = set()
backtrack(0, [])
print(len(combination))
