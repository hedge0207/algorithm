def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if anagrams.get(sorted_word):
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return anagrams.values()