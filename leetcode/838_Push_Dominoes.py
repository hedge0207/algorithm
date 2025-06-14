class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        after_pushed = [dominoes[0]]
        last_r_idx = 0 if dominoes[0] == "R" else -1
        for i in range(1, n):
            orig = dominoes[i]
            if orig == "R":
                if last_r_idx != -1:
                    for j in range(last_r_idx, len(after_pushed)):
                        after_pushed[j] = "R"
                last_r_idx = i
            elif orig == "L":
                j = len(after_pushed)-1
                while j >= 0 and after_pushed[j] == ".":
                    if last_r_idx != -1:
                        last_r_idx += 1
                    if j > last_r_idx:
                        after_pushed[j] = "L"
                    elif j < last_r_idx:
                        after_pushed[j] = "R"
                    j -= 1
                last_r_idx = -1
            after_pushed.append(orig)

        if last_r_idx != -1:
            for i in range(last_r_idx, len(after_pushed)):
                after_pushed[i] = "R"

        return "".join(after_pushed)