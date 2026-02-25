import re

class Solution:
    _pattern = re.compile(r'^[A-Za-z0-9_]+$')

    def _is_valid_code(self, code: str):
        return bool(self._pattern.match(code))

    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        category = {"electronics":[], "grocery":[], "pharmacy":[], "restaurant":[]}
        for i in range(len(code)):
            if not self._is_valid_code(code[i]):
                continue
            if businessLine[i] not in category:
                continue
            if not isActive[i]:
                continue

            category[businessLine[i]].append(code[i])
        ans = []
        for valid_code in category.values():
            ans += sorted(valid_code)
        return ans