import sys
sys.stdin = open("5252_input.txt", "r")

for tc in range(1, int(input()) + 1):
    A,B = map(int,input().split())
    words =[]
    for _ in range(A+B):
        word = input()
        if word not in words:
            words.append(word)
    print("#{} {}".format(tc,A+B-len(words)))

