n = int(input())
result = []
for i in range(1 << n):
    g = i ^ (i >> 1)
    result.append(format(g, f'0{n}b'))
for line in result:
    print(line)