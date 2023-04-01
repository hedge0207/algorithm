class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [1] + [0] * (n + forget)
        num_forget_people = 0

        for i in range(n + 1):
            for j in range(i + delay, i + forget):
                people[j] += people[i]
            num_forget_people += people[i - forget - 1]

        return (sum(people[:n]) - num_forget_people) % (10 ** 9 + 7)