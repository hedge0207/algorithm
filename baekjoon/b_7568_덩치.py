# 풀고 나서 생각해보니 굳이 dict를 쓸 필요가 없는 문제.
N = int(input())
people = {i: input().split(' ') for i in range(N)}
count_dict = {i: 0 for i in range(N)}

for person, body_info in people.items():
    person_w, person_h = body_info
    for other, others_body_info in people.items():
        if person == other:
            continue
        other_w, other_h = others_body_info
        if person_w < other_w and person_h < other_h:
            count_dict[person] += 1

for count in count_dict.values():
    print(count + 1, end=" ")


# 보다 나은 풀이
num = int(input())
val = []
for i in range(num):
    val.append(list(map(int, input().split())))

for i in val:
    rank = 1
    for j in val:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')


# 틀린 처음 코드
# 처음에는 낮은 사람들을 구하려고 했다.
N = int(input())
people = {i: input().split(' ') for i in range(N)}
count_dict = {i: 0 for i in range(N)}

for person, body_info in people.items():
    person_w, person_h = body_info
    for other, others_body_info in people.items():
        if person == other:
            continue
        other_w, other_h = others_body_info
        if person_w > other_w and person_h > other_h:
            count_dict[person] += 1

rank = 1
answer = [0] * N
while rank != N + 1:
    max_count = max(count_dict.values())
    cnt = 0
    for person, count in count_dict.items():
        if max_count == count:
            count_dict[person] = -1
            answer[person] = rank
            cnt += 1
    rank += cnt

for i in answer:
    print(i, end=" ")
