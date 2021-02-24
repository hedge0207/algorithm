import sys
N = int(input())
queue = []
for i in range(N):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        queue.append(command[1])
    else:
        if command[0] == "front":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif command[0] == "pop":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
                queue = queue[1:]
        elif command[0] == "size":
            print(len(queue))
        elif command[0] == "empty":
            if len(queue):
                print(0)
            else:
                print(1)
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
