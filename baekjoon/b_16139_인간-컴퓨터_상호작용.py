import sys

input = sys.stdin.readline
s = input()

num_alphabets = [[0]*26 for _ in range(len(s))]
num_alphabets[0][ord(s[0])-97] = 1
for i in range(1, len(s)):
    for j in range(26):
        if ord(s[i])-97 == j:
            num_alphabets[i][j] = num_alphabets[i-1][j] + 1
        else:
            num_alphabets[i][j] = num_alphabets[i-1][j]

n = int(input())
for _ in range(n):
    alphabet, i, j = input().split()
    i, j = int(i), int(j)
    idx = ord(alphabet)-97
    if i == 0:
        print(num_alphabets[j][idx])
    else:
        print(num_alphabets[j][idx]-num_alphabets[i-1][idx])