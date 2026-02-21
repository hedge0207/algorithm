class Solution:
    def compress(self, chars: list[str]) -> int:
        st = 0
        ed = 1
        cnt = 1
        while ed < len(chars):
            if chars[st] == chars[ed]:
                cnt += 1
                chars.pop(ed)
            else:
                if cnt > 1:
                    for num in str(cnt):
                        chars.insert(ed, num)
                        ed += 1
                cnt = 1
                st = ed
                ed = st+1
        if cnt > 1:
            for num in str(cnt):
                chars.insert(ed, num)
                ed += 1