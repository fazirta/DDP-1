class Bank:
    def __init__(self, name: str, interest: float = 0.0) -> None:
        self.name = name
        self.interest = interest


class SyariahBank(Bank):
    def __init__(self, name: str) -> None:
        super().__init__(name, 0.0)


class ConventionalBank(Bank):
    pass


class User:
    def __init__(self, balance: int, bank_account: Bank) -> None:
        self.balance = balance
        self.bank_account = bank_account

    def transfer_to(self, another_user: "User", amount: int):
        if another_user.bank_account is not self.bank_account:
            required_amount = amount + 6500
        else:
            required_amount = amount

        if self.balance < required_amount:
            print("Balance tidak cukup")
            return

        if another_user is self:
            print("Tidak bisa transfer ke dirinya sendiri")
            return

        if another_user is AdminBank:
            print("Tidak bisa transfer ke admin bank")
            return

        self.balance -= required_amount
        another_user.balance += amount

    def updateBalance(self, amount_of_month: int):
        self.balance += int(self.balance * self.bank_account.interest * amount_of_month)


class AdminBank(User):
    def __init__(self, bank: Bank):
        super().__init__(0, bank)

    def transfer_to(self, another_user: "User", amount: int):
        if another_user.bank_account is not self.bank_account:
            print("User di bank yang berbeda")
            return

        if another_user is self:
            print("Tidak bisa transfer ke dirinya sendiri")
            return

        if another_user is AdminBank:
            print("Tidak bisa transfer ke admin bank")
            return

        another_user.balance += amount

    def updateBalance(self, amount_of_month: int):
        print("Admin Bank tidak bisa updateBalance")


def display_balance(users: tuple[User, User, User, User]):
    print(f"User A Conven: {users[0].balance}")
    print(f"User B Conven: {users[1].balance}")
    print(f"User A Syariah: {users[2].balance}")
    print(f"User B Syariah: {users[3].balance}")
    print("==================")


conventional_bank = ConventionalBank("Bank konven", 0.1)
syariah_bank = SyariahBank("Syariahku")
user_a_conven = User(10000, conventional_bank)
user_b_conven = User(20000, conventional_bank)
user_a_syariah = User(10000, syariah_bank)
user_b_syariah = User(20000, syariah_bank)
admin_conven = AdminBank(conventional_bank)
admin_syariah = AdminBank(syariah_bank)
users = (user_a_conven, user_b_conven, user_a_syariah, user_b_syariah)

user_a_conven.transfer_to(user_b_conven, 20000)
display_balance(users)
user_a_conven.transfer_to(user_b_conven, 10000)
display_balance(users)
user_b_conven.transfer_to(user_a_syariah, 10000)
display_balance(users)
user_a_syariah.transfer_to(user_a_syariah, 10000)
display_balance(users)
user_b_syariah.transfer_to(user_a_syariah, 20000)
display_balance(users)
user_b_syariah.transfer_to(user_a_conven, 30000)
display_balance(users)
admin_conven.transfer_to(user_b_conven, 1000000000)
display_balance(users)
admin_syariah.transfer_to(user_a_syariah, 100000000)
display_balance(users)

user_a_conven.updateBalance(1)
user_b_conven.updateBalance(1)
user_a_syariah.updateBalance(1)
user_b_syariah.updateBalance(1)
display_balance(users)
