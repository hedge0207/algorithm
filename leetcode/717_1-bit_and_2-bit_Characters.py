class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        flag = False
        for i in range(len(bits)-1):
            if flag:
                flag = False
                continue
            if bits[i] == 1:
                flag = True
                continue
        return not flag