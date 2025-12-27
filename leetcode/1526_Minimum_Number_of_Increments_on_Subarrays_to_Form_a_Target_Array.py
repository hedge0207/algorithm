class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        dec_stack = [target[0]]
        ans = 0
        before = 0
        for i in range(1, len(target)):
            num = target[i]
            if dec_stack and dec_stack[-1] < num:
                ans += dec_stack[0] - before
                before = dec_stack[-1]
                dec_stack = [num]
            else:
                dec_stack.append(num)
            if i == len(target)-1:
                ans += dec_stack[0] - before
        return ans


# best_practice
class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        prev  = 0
        total = 0
        for i in target:
            if i > prev:
                total += i-prev
            prev = i
        return total