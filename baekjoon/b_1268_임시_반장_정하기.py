n, m = int(input()), 5
history = [list(map(int, input().split())) for _ in range(n)]
class_mates_per_student = {i:set() for i in range(n)}
for i in range(5):
    student_class = [set() for _ in range(10)]
    for j in range(n):
        student_class[history[j][i]].add(j)
    for students in student_class:
        for student in students:
            class_mates_per_student[student] = class_mates_per_student[student].union(students)
ans = 0
max_num = 0
for student, class_mates in class_mates_per_student.items():
    if len(class_mates) > max_num:
        max_num = len(class_mates)
        ans = student
print(ans+1)