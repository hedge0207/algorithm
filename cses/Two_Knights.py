move = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [-1, -2], [1, -2]]

n = int(input())
for k in range(1, n+1):
    total = ((k * k) * ((k * k)-1)) // 2
    attack = (2*(k-1)*(k-2)) + (2*(k-1)*(k-2))
    print(total-attack)