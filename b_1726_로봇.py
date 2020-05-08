#미완성

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def bfs():
    global Q, result
    cnt = 0
    visited = [[0] * C for _ in range(R)]
    dirr = sdi
    go = 0
    Q.append([sr, sc, dirr, cnt, go])
    visited[sr][sc] = 1
    while Q:
        NQ = []
        for q in Q:
            r, c, d, cn, g = q
            for i in range(4):
                flag = 0
                tc = cn
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                if factory[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    if dir_l[i] != d:
                        flag = 1
                        if abs(i-dir_l.index(d))==2:
                            tc+=2
                        else:
                            tc+=1
                        d = dir_l[i]
                    if flag:
                        NQ.append([nr, nc, d, tc,g+1])
                    else:
                        NQ.append([nr, nc, d, tc, g])
                    if nr == er and nc == ec:
                        visited[nr][nc]=0
                        ans = NQ[-1]
                        turn = ans[3]
                        if edi != ans[2]:
                            turn += 1
                        result = min(result,turn + ans[-1])
        Q = NQ



R, C = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(R)]
E = 1;W = 2;S = 3;N = 4
dir_l = [N, W, S, E]
sr, sc, sdi = map(int, input().split())
er, ec, edi = map(int, input().split())
sr -= 1
sc -= 1
er -= 1
ec -= 1
Q = []
result = 987654321
bfs()
if sr==er and sc== ec:
    if sdi==edi:
        print(0)
    else:
        if abs(dir_l.index(sdi) - dir_l.index(edi)) == 2:
            print(2)
        else:
            print(1)
else:
    print(result)