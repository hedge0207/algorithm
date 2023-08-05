import sys


def all_same(num, matrix):
    for row in matrix:
        for value in row:
            if num != value:
                return False
    return True

def cutting_paper(matrix, k):
    global result

    num = matrix[0][0]
    if all_same(num, matrix):
        result[num] += 1
        return

    k = k // 3
    for i in range(0, len(matrix), k):
        rows = matrix[i:i + k]
        for j in range(0, len(matrix), k):
            sub_matrix = [row[j:j + k] for row in rows]
            cutting_paper(sub_matrix, k)


input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]
cutting_paper(matrix, N)

print(result[-1])
print(result[0])
print(result[1])