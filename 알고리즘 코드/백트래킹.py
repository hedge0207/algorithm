# 1~9까지의 숫자가 들어 있는 집합의 부분 집합 중 합이 10인 부분집합 출력하기 

# 내 코드
def f(k, t, array):
    if t == 10:
        print(array)
        return
    if t >= 10 or k >= len(arr):
        return
    for i in range(k, len(arr)):
        if visited[i] == 0:
            visited[i] = 1
            array.append(arr[i])
            f(i, t + arr[i], array)
            array.pop()
            visited[i] = 0


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
visited = [0] * len(arr)
f(0, 0, [])



# 강사님 코드
def backtrack(arr, idx, N, selected, sum_num):
    if sum_num > 10:
        return
    if idx == N:
        if sum_num == 10:
            for i in range(N):
                if selected[i]:
                    print(arr[i], end=" ")
            print()
        return
    selected[idx] = 1
    backtrack(arr, idx + 1, N, selected, sum_num + arr[idx])
    selected[idx] = 0
    backtrack(arr, idx + 1, N, selected, sum_num)

backtrack(arr, 0, 9, [0] * 9, 0)
