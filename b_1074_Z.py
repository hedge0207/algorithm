#rs, re, cs, ce를 인덱스가 아닌 줄이라고 생각해라.
#예를 들어 4*4는 0번째 줄부터 4번째 줄까지 5개의 줄이 존재하는데 예제에서 찾는 (3,1)칸은 r의 3번째줄과 4번째줄 사이, c의 1번째 줄과 2번째 줄 사이에 위치한다.
def z(rs, re, cs, ce, cnt):
    if r == rs and c == cs:
        print(cnt)
        return

    rm = (rs + re) // 2
    cm = (cs + ce) // 2

    #이미 거친 사분면만큼 더해줘야 한다.2-1-3-4순으로 탐색하므로 예를 들어 4*4에서 답이 1사분면에 있다면 2사분면은 이미 거쳐왔다는 말이 된다.
    #따라서 한 사분면의 크기만큼을 더해줘야 한다. 마찬가지로 답이 3사분면에 있다면 2,4사분면을 이미 거쳐왔다는 의미이므로 두 사분면 만큼 더해줘야
    #한다. 즉 아래의 q는 한 사분면의 크기를 뜻한다.
    q = (rm - rs) * (cm - cs)

    # 4부분으로 나눠서 탐색하되 r과 c가 있는 부분만 계속 탐색해 나간다.
    #2사분면
    if rs <= r < rm and cs <= c < cm:
        z(rs, rm, cs, cm, cnt)
    #1사분면
    elif rs <= r < rm and cm <= c < ce:
        z(rs, rm, cm, ce, cnt + q)
    #3사분면
    elif rm <= r < re and cs <= c < cm:
        z(rm, re, cs, cm, cnt + q * 2)
    #4사분면
    elif rm <= r < re and cm <= c < ce:
        z(rm, re, cm, ce, cnt + q * 3)


n, r, c = map(int, input().split())
a = 2**n
#위의 재귀 부분을 보면 알겠지만 어차피 re,ce는 탐색 범위에 들어가지 않으므로 a-1이 아닌 a를 넣는다.
z(0, a, 0, a, 0)


