word = input()

n = len(word)
for i in range(n):
    l = i
    r = n-1
    while r > l:
        if word[l] == word[r]:
            r -= 1
            l += 1
        else:
            break
    else:
        break
print(n+i)