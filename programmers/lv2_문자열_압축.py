def solution(s):
    answer = len(s)
    for l in range(1, (len(s) // 2) + 1):
        prev = s[0:0 + l]
        i = l
        cnt = 1
        compressed_str = ""
        while 1:
            sub_string = s[i:i + l]
            if sub_string == prev:
                cnt += 1
            else:
                compressed_str += prev if cnt == 1 else str(cnt) + prev
                prev = sub_string
                cnt = 1
            if i + l > len(s):
                compressed_str += sub_string if cnt == 1 else str(cnt) + sub_string
                break
            i += l
        answer = min(answer, len(compressed_str))

    return answer