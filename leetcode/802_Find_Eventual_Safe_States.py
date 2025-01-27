# 재귀를 사용해야 할 경우 내부 함수를 사용하는 것이 더 깔끔하다.
# 노드의 방문 여부를 확인하는 배열과, 노드가 safe node인지를 확인하는 배열을 따로 관리했는데, 그럴 필요가 없다,
# terminal 노드를 먼저 구했는데, 더 이상 진행할 수 없으면 terminal 노드라는 의미이므로 이 역시 미리 구할 필요가 없다.
# 위 문제점들을 개선한 코드가 아래의 best_practice 코드이다.
class Solution:
    def __init__(self):
        self._graph = []
        self._terminal_nodes = []
        self._safety_nodes = []
        self._visited = []

    def _set_graph(self, graph: list[list[int]]):
        self._graph = graph

    def _set_terminal_nodes(self):
        for i, adjacent_nodes in enumerate(self._graph):
            if len(adjacent_nodes) == 0:
                self._terminal_nodes.append(i)

    def _set_visited(self):
        self._visited = [0] * len(self._graph)

    def _set_safety_nodes(self):
        self._safety_nodes = [None] * len(self._graph)

    def _is_safe_node(self, start_node: int, cur_node: int):
        if cur_node in self._terminal_nodes:
            return True

        result = False
        for adjacent_node in self._graph[cur_node]:
            if self._visited[adjacent_node] == 1:
                result = False
                break
            self._visited[adjacent_node] = 1
            if self._safety_nodes[adjacent_node] is None:
                result = self._is_safe_node(start_node, adjacent_node)
            else:
                result = self._safety_nodes[adjacent_node]
            self._visited[adjacent_node] = 0
            if not result:
                break

        self._safety_nodes[cur_node] = result
        return result

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        self._set_graph(graph)
        self._set_terminal_nodes()
        self._set_visited()
        self._set_safety_nodes()

        safe_nodes = self._terminal_nodes[:]
        for i in range(len(graph)):
            if i in self._terminal_nodes:
                continue
            if self._visited[i] == 1:
                continue
            self._visited[i] = 1
            is_safe_node = self._is_safe_node(i, i)
            self._visited[i] = 0
            self._safety_nodes[i] = is_safe_node
            if is_safe_node:
                safe_nodes.append(i)

        return sorted(safe_nodes)


# best_practice
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        visited = [0] * len(graph)

        def _is_safe_node(node: int):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1
            for adj_node in graph[node]:
                if not _is_safe_node(adj_node):
                    return False

            visited[node] = 2
            return True

        safe_nodes = []
        for i in range(len(graph)):
            if _is_safe_node(i):
                safe_nodes.append(i)

        return sorted(safe_nodes)