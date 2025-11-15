class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()

        n = len(potions)
        def binary_search(spell):
            st, ed = 0, n-1
            result = -1
            while st <= ed:
                mid = (st + ed) // 2
                if spell * potions[mid] >= success:
                    result = mid
                    ed = mid - 1
                else:
                    st = mid + 1
            return result

        ans = []
        for spell in spells:
            idx = binary_search(spell)
            if idx == -1:
                ans.append(0)
                continue
            ans.append(n-idx)
        return ans