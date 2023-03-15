import sys

input = sys.stdin.readline
opening, num_applicant = map(int, input().split())

apply_order = {}
for i in range(num_applicant):
    student_num = input().rstrip()
    apply_order[student_num] = i

apply_order = sorted(apply_order, key=lambda k: apply_order[k])
opening = min(opening, len(apply_order))
for i in range(opening):
    print(apply_order[i])
