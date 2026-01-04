class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for char in s:
            if count.get(char):
                count[char] += 1
            else:
                count[char] = 1

        ans = ""
        for i in range(len(order)):
            if count.get(order[i]):
                ans += order[i] * count.get(order[i])

        char_set = set(order)
        for char in s:
            if char in char_set:
                continue
            ans += char

        return ans