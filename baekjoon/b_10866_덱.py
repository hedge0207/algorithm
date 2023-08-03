import sys

class Deque:
    def __init__(self):
        self.elements = []

    def push_front(self, x):
        self.elements = [x] + self.elements

    def push_back(self, x):
        self.elements.append(x)

    def pop_front(self):
        if self.elements:
            print(self.elements[0])
            self.elements = self.elements[1:]
        else:
            print(-1)

    def pop_back(self):
        if self.elements:
            print(self.elements[-1])
            self.elements = self.elements[:-1]
        else:
            print(-1)

    def size(self):
        print(len(self.elements))

    def empty(self):
        print(0) if self.elements else print(1)

    def front(self):
        print(self.elements[0]) if self.elements else print(-1)

    def back(self):
        print(self.elements[-1]) if self.elements else print(-1)


if __name__ == "__main__":
    deque = Deque()
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        command = input().split()
        if len(command) == 2:
            if command[0] == "push_back":
                deque.push_back(command[1])
            elif command[0] == "push_front":
                deque.push_front(command[1])
        else:
            command = command[0]
            if command == "front":
                deque.front()
            elif command == "back":
                deque.back()
            elif command == "size":
                deque.size()
            elif command == "empty":
                deque.empty()
            elif command == "pop_front":
                deque.pop_front()
            else:
                deque.pop_back()