board = input()
ans = ""
length = 0
for mark in board:
    if mark == ".":
        if length % 2 == 1:
            ans = -1
            break
        ans += "AAAA" * (length//4)
        ans += "BB" * (length%4 // 2)
        length = 0
        ans += mark
    else:
        length += 1
if length % 2 == 1:
    ans = -1
else:
    ans += "AAAA" * (length // 4)
    ans += "BB" * (length % 4 // 2)
print(ans)