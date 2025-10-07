class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 1
        largest_num = -1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt == 3:
                if int(num[i-1]) > largest_num:
                    largest_num = int(num[i-1])

        if largest_num == -1:
            return ""
        else:
            return "".join([str(largest_num) for _ in range(3)])



