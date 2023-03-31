from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while (n := len(students)) != 0:
            flag = True
            for _ in range(n):
                if students[0] == sandwiches[0]:
                    flag = False
                    students = students[1:]
                    sandwiches = sandwiches[1:]
                    flag = False
                else:
                    students = students[1:] + [students[0]]
            if flag:
                break
        return len(students)
