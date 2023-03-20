class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine_letters(letter, idx, digits):
            if idx == len(digits):
                if letter:
                    result.append(letter)
                return

            if digits[idx] == "1":
                combine_letters(letter, idx + 1, digits)
            else:
                for char in letters_per_num[digits[idx]]:
                    combine_letters(letter + char, idx + 1, digits)


        letters_per_num = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        result = []

        combine_letters("", 0, digits)
        return result