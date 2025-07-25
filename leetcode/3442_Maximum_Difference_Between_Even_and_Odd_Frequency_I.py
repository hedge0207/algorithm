class Solution:
    def maxDifference(self, s: str) -> int:
        counter = {}
        for char in s:
            if counter.get(char):
                counter[char] += 1
            else:
                counter[char] = 1

        max_odd = 0
        min_even = 0
        for num in counter.values():
            if num % 2 == 0:
                if min_even == 0:
                    min_even = num
                else:
                    if min_even > num:
                        min_even = num
            else:
                if max_odd < num:
                    max_odd = num

        return max_odd - min_even

