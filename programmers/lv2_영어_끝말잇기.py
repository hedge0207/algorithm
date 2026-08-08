def solution(n, words):
    end_idx = 0
    used = {words[0]}
    for i in range(1, len(words)):
        last_word = words[i-1]
        word = words[i]
        if word in used or last_word[-1] != word[0]:
            end_idx = i
            break
        used.add(word)
    else:
        return [0, 0]

    return [(end_idx % n)+1, (end_idx//n)+1]