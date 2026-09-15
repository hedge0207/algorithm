class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        texts = [list(encodedText[i * cols : (i+1) * cols]) for i in range(rows)]

        ans = ""
        for i in range(cols):
            ans += texts[0][i]
            k = i + 1
            for j in range(1, rows):
                if k >= cols:
                    break
                ans += texts[j][k]
                k += 1
        return ans.rstrip()