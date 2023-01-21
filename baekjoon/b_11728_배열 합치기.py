N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Two pointer 사용
p1 = p2 = 0
merged_lst = []
while 1:
    if p1 == N:
        merged_lst += B[p2:]
        break
    if p2 == M:
        merged_lst += A[p1:]
        break

    if A[p1] > B[p2]:
        merged_lst.append(B[p2])
        p2 += 1
    else:
        merged_lst.append(A[p1])
        p1 += 1

for num in merged_lst:
    print(num, end=" ")


# 가장 단순한 풀이 Timsort 사용
# for num in sorted(A+B):
#     print(num, end=" ")
