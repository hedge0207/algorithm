n = int(input())
m = int(input())
recommended = list(map(int, input().split()))
frames = {}

for i in range(m):
    if recommended[i] not in frames:
        if len(frames) == n:
            student_to_remove = 0
            min_recommend = float("inf")
            order = n
            for recommended_student, info in frames.items():
                if info[0] < min_recommend:
                    student_to_remove = recommended_student
                    min_recommend = info[0]
                    order = info[1]
                elif info[0] == min_recommend:
                    if info[1] < order:
                        student_to_remove = recommended_student
            frames.pop(student_to_remove)
        frames[recommended[i]] = [1, i]
    else:
        frames[recommended[i]][0] += 1

for i in sorted(frames.keys()):
    print(i, end=" ")