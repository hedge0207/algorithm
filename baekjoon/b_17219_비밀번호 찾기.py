import sys

input = sys.stdin.readline
N, M = map(int, input().split())

password_per_site = {}
for _ in range(N):
    site, password = input().split()
    password_per_site[site] = password

for _ in range(M):
    site = input().rstrip()
    print(password_per_site[site])