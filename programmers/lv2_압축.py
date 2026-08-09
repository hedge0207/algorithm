def solution(msg):
    dictionary = {chr(i+ord("A")-1):i for i in range(1, 27)}
    answer = []
    last_idx = 27
    i = 0
    word = ""
    while i < len(msg):
        new_word = word + msg[i]
        if new_word in dictionary:
            word = new_word
            i += 1
            if i == len(msg):
                answer.append(dictionary[word])
        else:
            answer.append(dictionary[word])
            dictionary[new_word] = last_idx
            last_idx += 1
            word = ""
            new_word = ""
    return answer