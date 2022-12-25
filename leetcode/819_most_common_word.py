def mostCommonWord(paragraph: str, banned) -> str:
    preprocessed_paragraph = ""
    for char in paragraph:
        if char.isalnum():
            preprocessed_paragraph += char.lower()
        else:
            preprocessed_paragraph += " "
    word_list = preprocessed_paragraph.split(" ")

    common_word = ""
    pre_cnt = -1
    counted_words = [""]
    for word in word_list:
        if word not in banned and word not in counted_words:
            counted_words.append(word)
            num_word = word_list.count(word)
            if pre_cnt < num_word:
                common_word = word
                pre_cnt = num_word

    return common_word


# best_practice
# regexp, Counter
# def mostCommonWord(paragraph: str, banned):
#     words = [word for word in
#             re.sub(r'[^\w]', ' ', paragraph).lower().split()
#             if word not in banned]
#     counts = collections.Counter(words)
#     return counts.most_common(1)[0][0]

