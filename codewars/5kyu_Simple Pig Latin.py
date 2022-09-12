import string


def pig_it(text):
    text = text.split(" ")
    pig_words = []
    for word in text:
        if word[0] not in string.punctuation:
            word = "{}{}ay".format(word[1:], word[0])
        pig_words.append(word)

    return " ".join(pig_words)


print(pig_it("Hello world !"))


# best_practice
# isalpha 사용
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
