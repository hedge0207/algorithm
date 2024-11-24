def calculate_appearance(sub_string):
    appearance = {}
    for char in sub_string:
        if appearance.get(char):
            appearance[char] += 1
        else:
            appearance[char] = 1
    return appearance

def sherlockAndAnagrams(s):
    n = len(s)
    size = 1
    ans = 0
    while size < n:
        st = 0
        ed = st + size
        while ed < n:
            orig_appearance = calculate_appearance(s[st:ed])
            pst = st + 1
            ped = ed + 1
            while ped <= n:
                new_appearance = calculate_appearance(s[pst:ped])
                for char, num in orig_appearance.items():
                    if new_appearance.get(char) is None:
                        break
                    if new_appearance.get(char) != orig_appearance.get(char):
                        break
                else:
                    ans += 1
                pst += 1
                ped += 1
            st += 1
            ed += 1
        size += 1
    return ans