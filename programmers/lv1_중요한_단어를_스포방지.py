def solution(message, spoiler_ranges):
    n = len(message)
    is_spoiler = [0] * n
    for l, r in spoiler_ranges:
        for i in range(l, r+1):
            is_spoiler[i] = 1

    num_per_word = {}
    num_spoiler_per_word = {}

    st = 0
    while message[st] == " ":
        st += 1

    for word in message.split():
        ed = st + len(word)
        is_blind = False
        for i in range(st, ed):
            if is_spoiler[i]:
                is_blind = True
                break
        if num_per_word.get(word):
            num_per_word[word] += 1
        else:
            num_per_word[word] = 1
        if is_blind:
            if num_spoiler_per_word.get(word):
                num_spoiler_per_word[word] += 1
            else:
                num_spoiler_per_word[word] = 1
        st = ed + 1

    answer = 0
    for word, num in num_spoiler_per_word.items():
        if num == num_per_word[word]:
            answer += 1
    return answer