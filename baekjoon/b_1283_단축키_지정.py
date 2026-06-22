n = int(input())
options = [input().split() for _ in range(n)]
ans = []
reserved = set()
for option in options:
    for i in range(len(option)):
        word = option[i]
        if word[0].lower() in reserved:
            continue
        reserved.add(word[0].lower())
        option[i] = "[" + word[0] +"]" + word[1:]
        ans.append(" ".join(option))
        break
    else:
        word = " ".join(option)
        for i in range(len(word)):
            char = word[i].lower()
            if char == " ":
                continue
            if char in reserved:
                continue
            reserved.add(char)
            ans.append(word[:i] + "[" + word[i] + "]" + word[i+1:])
            break
        else:
            ans.append(word)
for word in ans:
    print(word)