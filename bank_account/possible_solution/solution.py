class BankAccount:
    defaultAccNumber = 1

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.accountnumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError
        else:
            self.balance -= amount

    def getBalance(self):
        return "${:,.2f}".format(self.balance)
