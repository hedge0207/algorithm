N = int(input())
nums = list(map(int, input().split()))
nums.sort()
max_num = nums[-1]
# 주어지는 수는 1000이하의 자연수
prime = [1] * (max_num + 1)

for i in range(2, 1001):
    for j in range(i, len(prime), i):
        if i == j:
            continue
        prime[j] = 0

cnt = 0
for i in range(2, len(prime[:max_num + 1])):
    if i in nums and prime[i] == 1:
        cnt += 1

print(cnt)
