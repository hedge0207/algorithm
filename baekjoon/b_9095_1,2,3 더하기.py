table = [0, 1, 2, 4] + [0] * 7

for i in range(4, len(table)):
    table[i] = table[i-1] + table[i-2] + table[i-3]

for _ in range(int(input())):
    n = int(input())
    print(table[n])