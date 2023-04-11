LIMIT = 10000
nums = [0] * (LIMIT + 1)

i = 0
while i < LIMIT:
    i += 1
    self_num = i + sum(map(int, list(str(i))))
    if self_num > LIMIT:
        continue
    nums[self_num] = 1


for i in range(1, LIMIT):
    if nums[i] == 0:
        print(i)
