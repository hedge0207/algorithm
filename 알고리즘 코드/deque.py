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