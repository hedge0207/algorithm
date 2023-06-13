import sys


def sort_schedule(schedule):
    return schedule[1], schedule[0]


input = sys.stdin.readline
N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
schedules.sort(key=sort_schedule)

cnt = 0
last_finish_time = 0
for schedule in schedules:
    if last_finish_time > schedule[0]:
        continue
    cnt += 1
    last_finish_time = schedule[1]

print(cnt)