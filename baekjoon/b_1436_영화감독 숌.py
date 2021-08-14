# N = int(input())
#
# cnt = 0
# num = 666
# answer = 0
# while True:
#     three_num = ''
#     six_count = 0
#     total_six_count = list(str(num)).count('6')
#     if total_six_count < 3:
#         num += 1
#         continue
#
#     iter_six_count = 0
#     for i in str(num):
#         if i == "6":
#             iter_six_count += 1
#             six_count += 1
#             if six_count == 3:
#                 cnt += 1
#                 break
#             continue
#         six_count = 0
#         if iter_six_count + 3 > total_six_count:
#             break
#
#     if cnt == N:
#         answer = num
#         break
#
#     num += 1
#
# print(answer)

N = int(input())
number = 666

while N:
    if "666" in str(number):
        N -= 1
    number += 1

print(number - 1)