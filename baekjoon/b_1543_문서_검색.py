doc = input()
term = input()

ans = 0
i = 0
while i <= len(doc)-len(term):
    if doc[i:i + len(term)] == term:
        ans += 1
        i += len(term)
    else:
        i += 1
print(ans)