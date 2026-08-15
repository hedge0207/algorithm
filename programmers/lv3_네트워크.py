def solution(n, computers):
    visited = [0] * n
    def dfs(d):
        for i in range(n):
            if computers[d][i] == 0:
                continue
            if visited[i] == 1:
                continue
            visited[i] = 1
            dfs(i)

    answer = 0
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer += 1
            dfs(i)
    return answer