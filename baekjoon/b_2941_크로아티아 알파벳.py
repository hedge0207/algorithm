croatian_alphabets = ["dz=", "c=", "s=", "z=", "c-", "d-", "lj", "nj"]

text = input()
cnt = 0
N = len(text)
tmp = 0

i = 0
while i < N:
    flag = False
    for j in range(i, i + 3):
        sub_str = text[i:j + 1]
        if sub_str in croatian_alphabets:
            tmp += len(sub_str)
            cnt += 1
            i = j + 1
            break
    else:
        i += 1

print(N - tmp + cnt)
