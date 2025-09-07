class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self._nums1 = nums1
        self._nums2 = nums2
        self._nums2_cnt = {}
        self._init_cnt()

    def _init_cnt(self):
        for num in self._nums2:
            if self._nums2_cnt.get(num):
                self._nums2_cnt[num] += 1
            else:
                self._nums2_cnt[num] = 1

    def add(self, index: int, val: int) -> None:

        self._nums2_cnt[self._nums2[index]] -= 1
        new_num = self._nums2[index]+val
        if self._nums2_cnt.get(new_num):
            self._nums2_cnt[new_num] += 1
        else:
            self._nums2_cnt[new_num] = 1
        self._nums2[index] += val

    def count(self, tot: int) -> int:
        ans = 0
        for num in self._nums1:
            num2 = tot-num
            if num2 <= 0:
                continue
            ans += self._nums2_cnt[num2] if self._nums2_cnt.get(num2) else 0
        return ans



















operations = ["FindSumPairs","count","add","count","count","add","add","count"]
params = [[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]
obj = None
for op, param in zip(operations, params):
    if op == "FindSumPairs":
        obj = FindSumPairs(*param)
    elif op == "add":
        obj.add(*param)
    else:
        obj.count(*param)