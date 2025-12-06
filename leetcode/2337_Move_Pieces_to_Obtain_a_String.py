class Solution:
    def canChange(self, start: str, target: str) -> bool:
        target_arr = []
        for i in range(len(target)):
            if target[i] == "L" or target[i] == "R":
                target_arr.append([target[i], i])

        start_arr = []
        for i in range(len(start)):
            if start[i] == "L" or start[i] == "R":
                start_arr.append([start[i], i])

        if len(target_arr) != len(start_arr):
            return False

        for i in range(len(target_arr)):
            if target_arr[i][0] != start_arr[i][0]:
                return False
            if target_arr[i][0] == "L" and target_arr[i][1] > start_arr[i][1]:
                return False
            if target_arr[i][0] == "R" and target_arr[i][1] < start_arr[i][1]:
                return False

        return True