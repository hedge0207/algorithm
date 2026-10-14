n, k = map(int, input().split())
s = input().strip()

segments = []
start = 0
for i in range(1, n):
    if s[i] != s[i-1]:
        segments.append(s[start:i])
        start = i
segments.append(s[start:n])

result = []
one_count = 0
i = 0
while i < len(segments):
    result.append(segments[i])
    if segments[i][0] == "1":
        one_count += 1
        if one_count == k-1 and i + 2 < len(segments):
            result.append(segments[i+2])
            result.append(segments[i+1])
            i += 3
            continue
    i += 1

print("".join(result))