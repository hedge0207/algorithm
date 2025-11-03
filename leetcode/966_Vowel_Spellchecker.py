from collections import defaultdict


class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        words_set = set(wordlist)
        words = defaultdict(list)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for word in wordlist:
            new_word = ""
            lower = ""
            for char in word:
                if char in vowels:
                    new_word += "1"
                else:
                    new_word += char.lower()
                lower += char.lower()
            words[new_word].append(word)
            words[lower].append(word)

        ans = []
        for query in queries:
            new_query = ""
            if query in words_set:
                ans.append(query)
                continue
            if query.lower() in words:
                ans.append(words.get(query.lower())[0])
                continue
            for char in query:
                if char in vowels:
                    new_query += "1"
                else:
                    new_query += char.lower()
            if words.get(new_query):
                ans.append(words[new_query][0])
            else:
                ans.append("")

        return ans


