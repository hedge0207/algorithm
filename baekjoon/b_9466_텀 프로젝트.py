# 총 10시간 만에 통과, pypy로 제출하면 메모리 초과가, python으로 제출하면 시간초과가 떠서 시간 초과를 피하기 위해 여러 시도를
# 하느라 시간이 많이 걸렸다.
# 다른 사람 코드를 참고하여 통과한 코드
# 2번 코드와 다른 점은 in연산을 매 재귀마다 수행하는 것이 아니라 visited[n]이 0이 아닐 경우에만 수행하는 것으로 바꿈
# 리스트에서 in연산은 시간복잡도가 O(N)으로 생각보다 시간을 많이 잡아먹는 다는 것을 처음 알게 되었다.
import sys
sys.setrecursionlimit(1000000)

def f(x,l):
    global cnt
    l.append(x)
    visited[x] = 1
    n = G[x]

    if visited[n]:
        if n in l:
            cnt+=len(l[l.index(G[x]):])
        return

    if visited[n]==0:
        f(n,l)

for tc in range(int(input())):
    N = int(input())
    G = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (N + 1)

    cnt = 0
    for i in range(1, len(G)):
        if visited[i] == 0:
            f(i,[])

    print(N-cnt)

#2번 코드
#1번 코드가 계속 시간초과가 발생해 다시 짠 코드, 여전히 80% 언저리에서 시간초과가 발생했다.
import sys
sys.setrecursionlimit(1000000)

def f(x,l):
    global result
    l.append(x)
    visited[x] = 1
    n = G[x]

    if n in l:
        result+=l[l.index(G[x]):]
        return

    if visited[n]==0:
        f(n,l)

for tc in range(int(input())):
    N = int(input())
    G = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (N + 1)

    result = []
    for i in range(1, len(G)):
        if visited[i] == 0:
            f(i,[])

    print(N-len(result))

# 1번 코드
# 계속 시간초과가 뜬 코드-1
# 7시간 동안 시도해봤으나 이 코드로는 불가능하다고 생각해 다시 코드를 짰다.
# 최초 함수에 들어간 s값과 재귀를 통해 들어간 e값이 같으면 사이클이 있다고 판단.
# 이 코드의 문제점: 불필요한 반복이 너무 많이 일어난다. 예를들어 3 1 4 3일 경우 이 처음 1로 들어갔을 때 3과 4사이에 사이클이
# 있다는 것을 알아낼 수 있지만 이 코드로는 알아내지 못한다. 따라서 3도 다시 반복해 봐야하므로 불필요한 반복이 발생한다.
# 답은 맞은 것 같으나 80% 언저리에서 시간초과가 발생
# import sys
# sys.setrecursionlimit(1000000)
#
# def f(s, e, c):
#     global cnt, flag
#     if s == G[e]:
#         cnt += c
#         flag = 1
#         return
#
#     if visited[G[e]] == 0:
#         visited[G[e]] = 1
#         f(s, G[e], c + 1)
#         if not flag:
#             visited[G[e]] = 0
#
# for tc in range(int(input())):
#     N = int(input())
#     G = [0] + list(map(int, sys.stdin.readline().split()))
#     visited = [0] * (N + 1)
#
#     cnt = 0
#     for i in range(1, len(G)):
#         if i == G[i]:
#             visited[i] = 1
#             cnt += 1
#         elif visited[i] == 0:
#             flag = 0
#             visited[i] = 1
#             f(i, i, 1)
#
#     print(N - cnt)