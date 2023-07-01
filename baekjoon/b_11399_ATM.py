import sys

input = sys.stdin.readline
N = int(input())
line = sorted(list(map(int, input().split())))

total_time = 0
result = 0
for task_time in line:
    total_time = total_time + task_time
    result += total_time

print(result)