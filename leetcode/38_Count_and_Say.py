class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        post_count = self.countAndSay(n-1)
        string = ""
        chars = post_count[0]
        for i in range(1, len(post_count)):
            if chars[-1] != post_count[i]:
                string += f"{len(chars)}{chars[-1]}"
                chars = post_count[i]
            else:
                chars += post_count[i]
        string += f"{len(chars)}{chars[-1]}"

        return string