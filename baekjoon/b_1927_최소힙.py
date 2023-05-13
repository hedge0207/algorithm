import sys


class Heap:
    def __init__(self):
        self.nodes = [None]

    def __len__(self):
        return len(self.nodes) - 1

    def _percolate_up(self):
        idx = len(self)
        parent_idx = idx // 2
        while parent_idx > 0:
            if self.nodes[idx] < self.nodes[parent_idx]:
                self.nodes[idx], self.nodes[parent_idx] = self.nodes[parent_idx], self.nodes[idx]
                idx = parent_idx
                parent_idx //= 2
            else:
                break

    def insert(self, val):
        self.nodes.append(val)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        len_nodes = len(self)
        if left <= len_nodes and self.nodes[smallest] > self.nodes[left]:
            smallest = left

        if right <= len_nodes and self.nodes[smallest] > self.nodes[right]:
            smallest = right

        if smallest != idx:
            self.nodes[idx], self.nodes[smallest] = self.nodes[smallest], self.nodes[idx]
            self._percolate_down(smallest)

    def extract(self):
        len_nodes = len(self)
        if len_nodes == 0:
            return None
        min_value = self.nodes[1]
        self.nodes[1] = self.nodes[len_nodes]
        self.nodes.pop()
        self._percolate_down(1)
        return min_value


input = sys.stdin.readline
heap = Heap()
N = int(input())
for _ in range(N):
    operator = int(input())
    if operator:
        heap.insert(operator)
    else:
        if ans := heap.extract():
            print(ans)
        else:
            print(0)