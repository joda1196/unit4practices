class BankAccount:
    accnumber = 1

    def __init__(self, name):
        self.name = name
        self.accountnumber = BankAccount.accnumber
        self.balance = 0
        BankAccount.accnumber += 1

    def deposit(self, amount: int):
        self.balance += amount

    def getBalance(self):
        return "${:,.2f}".format(self.balance)

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError
        else:
            self.balance -= amount
