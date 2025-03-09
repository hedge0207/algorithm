class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        nums = set(nums)
        result = ""

        def recur(binary_string):
            nonlocal result

            if result:
                return

            if len(binary_string) == n:
                if binary_string not in nums:
                    result = binary_string
                return

            for bit in range(2):
                recur(binary_string + str(bit))

        recur("")
        return result