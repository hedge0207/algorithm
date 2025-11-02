from collections import defaultdict
import heapq


class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self._task_map = defaultdict(list)
        self._heap = []
        for task in tasks:
            user_id, task_id, priority = task
            self._task_map[task_id] = [priority, user_id]
            heapq.heappush(self._heap, [(-priority, -task_id), priority, task_id])

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        self._task_map[task_id] = [priority, user_id]
        heapq.heappush(self._heap, [(-priority, -task_id), priority, task_id])

    def edit(self, task_id: int, new_priority: int) -> None:
        self._task_map[task_id][0] = new_priority
        heapq.heappush(self._heap, [(-new_priority, -task_id), new_priority, task_id])

    def rmv(self, task_id: int) -> None:
        self._task_map.pop(task_id)

    def execTop(self) -> int:
        while len(self._heap) != 0:
            _, priority, task_id = heapq.heappop(self._heap)
            if self._task_map.get(task_id) is None:
                continue

            if self._task_map[task_id][0] != priority:
                heapq.heappush(self._heap, [(-self._task_map[task_id][0], -task_id), self._task_map[task_id][0], task_id])
                continue
            return self._task_map.pop(task_id)[1]

        return -1