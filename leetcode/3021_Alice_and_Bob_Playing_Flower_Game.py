class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        num_n_even = n // 2
        num_n_odd = num_n_even + 1 if n % 2 else num_n_even

        num_m_even = m // 2
        num_m_odd = num_m_even + 1 if m % 2 else num_m_even

        return num_n_even * num_m_odd + num_m_even * num_n_odd