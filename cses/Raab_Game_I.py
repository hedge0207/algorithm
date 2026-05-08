def raab_game(n, a, b):
    if a + b > n:
        print("NO")
        return
    if a+b == 1:
        print("NO")
        return
    if a+b >= 2 and (a==0 or b==0):
        print("NO")
        return

    draw = n-a-b
    cards = [i for i in range(n)]

    ans_a = []
    ans_b = []
    for i in range(draw):
        ans_a.append(i)
        ans_b.append(i)

    cards = cards[draw:]
    for i in range(len(cards)):
        ans_a.append(cards[i])
        ans_b.append(cards[(i+a)%len(cards)])

    print("YES")
    for i in ans_a:
        print(i+1, end=" ")
    print()
    for i in ans_b:
        print(i+1, end=" ")
    print()

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    raab_game(n, a, b)