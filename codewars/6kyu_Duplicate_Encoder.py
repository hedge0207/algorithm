def duplicate_encode(word):
    word = word.lower()
    answer = ""
    for i in word:
        if word.count(i) >= 2:
            answer += ")"
        else:
            answer += "("
    return answer

print(duplicate_encode("(( @"))
