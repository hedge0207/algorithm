class Solution:
    mapping_digit_to_letter = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    def letterCombinations(self, digits: str) -> list[str]:
        answer = []

        def combine(depth, combination):
            if depth == len(digits):
                if combination:
                    answer.append(combination)
                return

            for char in self.mapping_digit_to_letter[digits[depth]]:
                combine(depth + 1, combination + char)

        combine(0, "")
        return answer