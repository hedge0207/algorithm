import sys

input = sys.stdin.readline
N, M = map(int, input().split())

pokemons_num = {}
num_pokemons = {}
for i in range(1, N + 1):
    pokemon = input().rstrip()
    pokemons_num[pokemon] = i
    num_pokemons[i] = pokemon


for _ in range(M):
    data = input().rstrip()
    if data.isdigit():
        print(num_pokemons[int(data)])
    else:
        print(pokemons_num[data])

