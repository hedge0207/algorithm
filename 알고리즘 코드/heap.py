class MinHeap:
    def __init__(self):
        # index 기반 연산의 편의를 위해 0번 index는 사용하지 않는다.
        self.nodes = [None]

    def __len__(self):
        # node의 개수를 가지고 하는 연산이 많아 __len__ 메서드를 구현한다.
        return len(self.nodes) - 1

    # 삽입시에 사용하는 method로, 부모 노드와 값을 비교하면서 노드를 교환하는 과정이다.
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

    # 삭제시에 사용하는 method로, 좌, 우 노드와 값을 비교하면서 노드를 교환하는 과정이다.
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
        """
        최솟값을 반환하고 최소 힙에 맞게 재구성한다.
        """
        len_nodes = len(self)
        if len_nodes == 0:
            return None
        # 최소값(root)을 구한다.
        min_value = self.nodes[1]
        # 첫 노드의 값을 마지막 노드로 변경하고
        self.nodes[1] = self.nodes[len_nodes]
        # 마지막 노드를 삭제한다.
        self.nodes.pop()
        # 힙을 재구성한다.
        self._percolate_down(1)
        return min_value