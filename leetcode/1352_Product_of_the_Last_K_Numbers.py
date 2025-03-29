from collections import defaultdict

class ProductOfNumbers:

    def __init__(self):
        self._nums = []
        self._cache = defaultdict(int)

    def add(self, num: int) -> None:
        self._nums.append(num)
        self._cache = defaultdict(int)

    def getProduct(self, k: int) -> int:
        if self._cache.get(k):
            return self._cache[k]
        product = 1
        for num in self._nums[-k:]:
            product *= num
        self._cache[k] = product
        return product


# best practice
class ProductOfNumbers:

    def __init__(self):
        self.pre_mul = []
        self.product = 1

    def add(self, num: int) -> None:
        if num is not 0:
            self.product *= num
            self.pre_mul.append(self.product)
        else:
            self.product = 1
            self.pre_mul = []

    def getProduct(self, k: int) -> int:
        if k == len(self.pre_mul):
            return self.pre_mul[-1]
        elif k > len(self.pre_mul):
            return 0
        else:
            return int(self.pre_mul[-1] / self.pre_mul[-1 - k])