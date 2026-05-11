code_per_char = {
    "000000": "A",
    "001111": "B",
    "010011": "C",
    "011100": "D",
    "100110": "E",
    "101001": "F",
    "110101": "G",
    "111010": "H"
}

n = int(input())
letter = input()
ans = ""
for i in range(0, len(letter), 6):
    if code_per_char.get(letter[i:i+7]):
        ans += code_per_char[letter[i:i+7]]
    else:
        for code in code_per_char.keys():
            diff_cnt = 0
            for j in range(6):
                if code[j] != letter[i+j]:
                    if diff_cnt > 0:
                        break
                    else:
                        diff_cnt += 1
            else:
                ans += code_per_char[code]
                break
        else:
            ans = i // 6 + 1
            break

print(ans)