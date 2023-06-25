from typing import List
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_tasks = defaultdict(int)
        waitings = {}
        for task in tasks:
            num_tasks[task] += 1
            if task not in waitings:
                waitings[task] = 0

        result = 0
        cnt = 0
        while cnt < len(num_tasks):
            max_cnt = -1
            max_task = None
            for task, waiting_time in waitings.items():
                remain_num = num_tasks[task]
                if remain_num and waiting_time <= 0:
                    if remain_num > max_cnt:
                        max_cnt = remain_num
                        max_task = task
                waitings[task] -= 1
            if max_task:
                num_tasks[max_task] -= 1
                if num_tasks[max_task] == 0:
                    cnt += 1
                waitings[max_task] = n
            result += 1

        return result
