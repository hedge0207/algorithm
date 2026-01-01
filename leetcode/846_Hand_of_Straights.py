class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        n = len(hand) // groupSize
        used = [0] * len(hand)
        hand.sort()
        num_group = 0
        i = 0
        cnt = 0
        last_num = 0
        while i < len(hand):
            if used[i] == 1:
                i += 1
                continue
            if cnt == 0 or hand[i] == last_num+1:
                used[i] = 1
                last_num = hand[i]
                cnt += 1
            if cnt == groupSize:
                cnt = 0
                i = -1
                last_num = 0
                num_group += 1
            i += 1
        return n == num_group