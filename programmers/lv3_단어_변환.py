from collections import defaultdict, deque

def solution(begin, target, words):
    words.append(begin)
    n = len(words[0])
    graph = defaultdict(list)
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            diff = 0
            for z in range(n):
                if words[i][z] != words[j][z]:
                    diff += 1
                if diff == 2:
                    break
            else:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    queue = deque([[begin, 0]])
    visited = {word:0 for word in words}
    visited[begin] = 1
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for neighbor in graph[word]:
            if visited[neighbor]:
                continue
            visited[neighbor] = 1
            queue.append([neighbor, cnt + 1])
    return 0