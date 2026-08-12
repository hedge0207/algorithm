def solution(str1, str2):
    str1 = str1.lower()
    count1 = {}
    for i in range(0, len(str1)-1):
        char1, char2 = str1[i], str1[i+1]
        char1_cd = ord(char1)
        char2_cd = ord(char2)
        if char1_cd < 97 or char1_cd > 122 or char2_cd < 97 or char2_cd > 122:
            continue
        element = char1+char2
        if count1.get(element) is None:
            count1[element] = 1
        else:
            count1[element] += 1

    str2 = str2.lower()
    count2 = {}
    for i in range(0, len(str2)-1):
        char1, char2 = str2[i], str2[i+1]
        char1_cd = ord(char1)
        char2_cd = ord(char2)
        if char1_cd < 97 or char1_cd > 122 or char2_cd < 97 or char2_cd > 122:
            continue
        element = char1+char2
        if count2.get(element) is None:
            count2[element] = 1
        else:
            count2[element] += 1

    intersection = {}
    union = {}
    for k, v in count1.items():
        if count2.get(k):
            intersection[k] = min(v, count2.get(k))
            union[k] = max(v, count2.get(k))
        else:
            union[k] = v

    for k, v in count2.items():
        if count1.get(k) is None:
            union[k] = v

    if len(union) == 0:
        return 65536

    return int((sum(intersection.values()) / sum(union.values()))*65536)