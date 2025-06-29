# 못 풀고 포기, 다시 풀 필요는 없음
from collections import defaultdict


# time limit
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        nums_per_char = defaultdict(int)
        for char in s:
            nums_per_char[ord(char)] += 1

        for _ in range(t):
            new = defaultdict(int)

            for ascii_cd, num in nums_per_char.items():
                for i in range(1, nums[ascii_cd-ord("a")]+1):
                    new_cd = ((ascii_cd + i) - ord("a")) % 26 + ord("a")
                    new[new_cd] += num
            nums_per_char = new


        return sum(nums_per_char.values()) % (10**9 + 7)





MOD = 10**9 + 7

def mat_mult(A, B):
    size = len(A)
    result = [[0]*size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            if A[i][k] == 0:
                continue
            for j in range(size):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def mat_pow(M, power):
    size = len(M)
    result = [[int(i == j) for j in range(size)] for i in range(size)]  # identity matrix
    while power:
        if power % 2 == 1:
            result = mat_mult(result, M)
        M = mat_mult(M, M)
        power //= 2
    return result

def vector_mult(v, M):
    size = len(v)
    result = [0] * size
    for i in range(size):
        for j in range(size):
            result[i] = (result[i] + v[j] * M[j][i]) % MOD
    return result


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        size = 26
        count = [0] * size
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # 전이 행렬 생성
        M = [[0]*size for _ in range(size)]
        for i in range(size):
            for step in range(1, nums[i]+1):
                to = (i + step) % size
                M[i][to] = (M[i][to] + 1) % MOD

        # 전이 행렬을 t 제곱
        M_exp = mat_pow(M, t)

        # 벡터에 곱해서 최종 상태 계산
        final_count = vector_mult(count, M_exp)

        return sum(final_count) % MOD