class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if int(str(k)[-1]) not in [1, 3, 7, 9]:
            return -1

        mod, mod_set = 0, set()
        for length in range(1, k + 1):
            mod = (10 * mod + 1) % k
            if mod == 0:
                return length
            if mod in mod_set:
                return -1
            mod_set.add(mod)
        return -1