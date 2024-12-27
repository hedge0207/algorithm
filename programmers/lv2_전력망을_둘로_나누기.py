def check(n, elect_net):
    visited = [0] * (n + 1)
    ncnt = 0
    for i in range(1, len(elect_net)+1):
        if visited[i]:
            continue
        visited[i] = 1
        cnt = 1
        queue = [i]
        while queue:
            nqueue = []
            for q in queue:
                for node in elect_net[q]:
                    if visited[node]:
                        continue
                    visited[node] = 1
                    nqueue.append(node)
            cnt += len(nqueue)
            queue = nqueue
        if ncnt != 0:
            return abs(ncnt-cnt)
        ncnt = cnt

    return n

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        elect_net = {i: [] for i in range(1, n + 1)}
        for j in range(len(wires)):
            if i == j:
                continue
            s, t = wires[j]
            elect_net[s].append(t)
            elect_net[t].append(s)

        answer = min(answer, check(n, elect_net))

    return answer