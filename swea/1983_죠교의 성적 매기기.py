import sys
sys.stdin=open("1983_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    grade = [list(map(int, input().split())) for i in range(N)]

    total = []
    for i in range(len(grade)):
        a = 0
        for j in range(3):
            if j == 0:
                a += grade[i][j] * 0.35
            elif j == 1:
                a+= grade[i][j]*0.45
            else:
                a+=grade[i][j]*0.20
        total += [a]
    # print(total)
    c = total[K-1]
    for i in range(len(total)-1):
        for j in range(len(total)-i-1):
            if total[j] < total[j+1]:
                total[j], total[j+1] = total[j+1], total[j]

    aa = [0]*len(total)
    for i in range(len(total)):
        if (i+1) / len(total) <= 0.1:
            aa[i] = "A+"
        elif (i+1) / len(total) <= 0.2:
            aa[i] = "A0"
        elif (i+1) / len(total) <= 0.3:
            aa[i] = "A-"
        elif (i+1) / len(total) <= .04:
            aa[i] = "B+"
        elif (i+1) / len(total) <= 0.5:
            aa[i] = "B0"
        elif (i+1) / len(total) <= 0.6:
            aa[i] = "B-"
        elif (i+1) / len(total) <= 0.7:
            aa[i] = "C+"
        elif (i+1) / len(total) <= 0.8:
            aa[i] = "C0"
        elif (i+1) / len(total) <= 0.9:
            aa[i] = "C-"
        else:
            aa[i] = "D0"


    for i in range(len(total)):
        if c == total[i]:
            ans = aa[i]
    print(ans)





#노가다가 아닌 인덱스로 푼 해답
# T = int(input())
#
# for t in range(1, T + 1):
#     N, K = map(int, input().split())
#
#     each_score = [list(map(int, input().split())) for _ in range(N)]
#     grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
#     total_score = []
#
#     for i in range(N):
#         mid = each_score[i][0] * 0.35
#         final = each_score[i][1] * 0.45
#         homework = each_score[i][2] * 0.20
#
#         total = mid + final + homework
#
#         total_score.append(total)
#
#     check_student = total_score[K - 1]
#     total_score.sort()
#     total_score.reverse()
#
#     index = total_score.index(check_student)
#     n_index = index // (N // 10)
#
#
#     print('#%d' % t, grade[n_index])



