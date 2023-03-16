import sys

input = sys.stdin.readline

num_group, num_question = map(int, input().split())

groups = {}
for _ in range(num_group):
    group_name = input().rstrip()
    groups[group_name] = sorted(input().rstrip() for _ in range(int(input())))

for _ in range(num_question):
    name = input().rstrip()
    type_ = int(input())
    if type_:
        for group_name, members in groups.items():
            if name in members:
                print(group_name)
                continue
    else:
        for member in groups[name]:
            print(member)
