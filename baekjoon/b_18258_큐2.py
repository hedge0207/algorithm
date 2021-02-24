# 10845_큐 문제와 같은 방식으로 풀면 시간초과가 발생
# deque을 사용하는 방법도 있지만, 사용하고 싶지 않다면 아래와 같이 front의 인덱스를 가리키는 변수를 설정하면 된다.
# 시간초과가 발생하는 이유는 pop이 일어날 때마다 리스트 전체가 새로 만들어지기 때문으로 front를 가리키는 인덱스를 사용하면 굳이 pop을 하지 않아도 된다.
import sys

N = int(sys.stdin.readline())
queue = []
idx = 0
for i in range(N):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        queue.append(command[1])
    else:
        if command[0] == "front":
            if idx == len(queue):
                print(-1)
            else:
                print(queue[idx])
        elif command[0] == "pop":
            if idx == len(queue):
                print(-1)
            else:
                print(queue[idx])
                idx += 1
        elif command[0] == "size":
            print(len(queue)-idx)
        elif command[0] == "empty":
            if idx == len(queue):
                print(1)
            else:
                print(0)
        else:
            if idx == len(queue):
                print(-1)
            else:
                print(queue[-1])
