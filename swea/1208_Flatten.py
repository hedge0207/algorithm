import sys

sys.stdin = open("1208_input.txt", "r")

for tc in range(1, 11):
    dump_cnt = int(input())
    boxs = list(map(int, input().split()))

    for _ in range(dump_cnt):
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if boxs[i] > boxs[max_idx]:
                max_idx = i
            if boxs[i] < boxs[min_idx]:
                min_idx = i
        boxs[max_idx] -= 1
        boxs[min_idx] += 1

    max_height = 0
    min_height = 101
    for i in range(100):
        if max_height < boxs[i]:
            max_height = boxs[i]
        if min_height > boxs[i]:
            min_height = boxs[i]

    print("#{} {}".format(tc, max_height - min_height))
