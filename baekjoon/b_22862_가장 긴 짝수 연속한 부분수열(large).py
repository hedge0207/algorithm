import sys


input = sys.stdin.readline
N, k = map(int, input().split())
nums = list(map(int, input().split()))

st = 0
ed = 0
max_length = 0
length = 0
while st <= ed < N:
    if nums[ed] % 2 == 0:
        length += 1
        ed += 1
    else:
        if k != 0:
            ed += 1
            k -= 1
        else:
            if nums[st] % 2 == 0:
                length -= 1
            else:
                k += 1
            st += 1

    max_length = max(length, max_length)

print(max_length)


