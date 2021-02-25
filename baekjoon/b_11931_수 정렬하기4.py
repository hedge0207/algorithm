# quick 정렬로 풀려 했으나 시간 초과 발생
import sys

print(*sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse = True))