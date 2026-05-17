num_players = int(input())
num_rows = int(input())
result = input()
rows = [input() for _ in range(num_rows)]

over = [chr(i+65) for i in range(num_players)]
for i in range(num_rows):
    if rows[i][0] == "?":
        break
    for j in range(len(rows[0])):
        if rows[i][j] == "-":
            over[j], over[j+1] = over[j+1], over[j]

under = [char for char in result]
for i in range(num_rows-1, -1, -1):
    if rows[i][0] == "?":
        break
    for j in range(len(rows[0])):
        if rows[i][j] == "-":
            under[j], under[j+1] = under[j+1], under[j]

ans = ""
i = 0
while i < num_players-1:
    if over[i] == under[i]:
        ans += "*"
    else:
        if over[i] == under[i+1] and over[i+1] == under[i]:
            ans += "-"
            i += 1
            if i < num_players-1:
                ans += "*"
        else:
            print("x" * (num_players-1))
            break
    i += 1
else:
    print(ans)