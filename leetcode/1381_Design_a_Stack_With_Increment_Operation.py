class CustomStack:

    def __init__(self, maxSize: int):
        self._max_size = maxSize
        self._stack = []

    def push(self, x: int) -> None:
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self) -> int:
        if self._stack:
            return self._stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val