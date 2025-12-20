class Bank:

    def __init__(self, balance: list[int]):
        self._balance = balance
        self._n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 < account1 <= self._n and 0 < account2 <= self._n:
            if self._balance[account1-1] >= money:
                self._balance[account1-1] -= money
                self._balance[account2-1] += money
                return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 < account <= self._n:
            self._balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 < account <= self._n:
            if self._balance[account-1] - money >= 0:
                self._balance[account-1] -= money
                return True
        return False