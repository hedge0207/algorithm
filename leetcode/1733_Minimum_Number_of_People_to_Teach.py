class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        unmatched_user_set = set()
        for user1, user2 in friendships:
            if set(languages[user1-1]) & set(languages[user2-1]):
                continue
            unmatched_user_set.add(user1)
            unmatched_user_set.add(user2)

        if len(unmatched_user_set) == 0:
            return 0

        known_languages = {}
        for user in unmatched_user_set:
            for lang in languages[user-1]:
                if lang in known_languages:
                    known_languages[lang] += 1
                else:
                    known_languages[lang] = 1
        ans = len(languages)
        for num in known_languages.values():
            ans = min(len(unmatched_user_set)-num, ans)
        return ans