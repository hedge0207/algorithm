import sys
n = int(input())
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

#위와 같이 sys.stdin.readline()를 통해 입력을 받으면 입력 받는 속도가 빨라져 속도를 줄이는데 도움이 된다.



#아래 코드는 시간초과가 발생
# n = int(input())
# for _ in range(n):
#     a,b = map(int, input().split())
#     print(a+b)
