chars = input()

ans = set()
visited = [0] * len(chars)
def create_string(string):
    if len(string) == len(chars):
        ans.add(string)
        return

    for i in range(len(chars)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        create_string(string + chars[i])
        visited[i] = 0

create_string("")
ans = sorted(list(ans))
print(len(ans))
for string in ans:
    print(string)

