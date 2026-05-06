class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(1, n):
            inverted = ""
            for bit in s:
                if bit == "0":
                    inverted += "1"
                else:
                    inverted += "0"
            s = s + "1" + inverted[::-1]
        return s[k-1]