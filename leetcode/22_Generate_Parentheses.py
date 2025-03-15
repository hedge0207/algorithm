class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def gen_paren(n, k, num_open, num_close, paren_pair):
            if k == n:
                result.append(paren_pair)
                return

            if num_open < n // 2:
                gen_paren(n, k+1, num_open+1, num_close, paren_pair+"(")
            if num_open > num_close:
                gen_paren(n, k+1, num_open, num_close+1, paren_pair+")")
        gen_paren(n*2, 0, 0, 0, "")
        return result