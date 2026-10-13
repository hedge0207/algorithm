s = input()
cnt = {i: 0 for i in range(1,4)}
for digit in s:
    digit = int(digit)
    if digit not in cnt:
        break
    cnt[digit] += 1

for i in range(1,4):
    if cnt[i] != i:
        print("No")
        break
else:
    print("Yes")