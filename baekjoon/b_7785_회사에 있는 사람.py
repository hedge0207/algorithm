import sys


input = sys.stdin.readline

N = int(input())
remaining_people = {}
for _ in range(N):
    name, _ = input().split()
    if name in remaining_people:
        del remaining_people[name]
    else:
        remaining_people[name] = 1

sorted_names = sorted(remaining_people.keys(), reverse=True)
for name in sorted_names:
    print(name)