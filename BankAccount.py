class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        total = super().deposit(amount)
        print(f"Titular: {self.holder_name} | Depósito: ${amount} | Saldo total: ${total}")


class BusinessAccount(BankAccount):
    def deposit(self, amount):
        total = super().deposit(amount)
        print(f"Empresa: {self.holder_name} | Depósito: ${amount} | Saldo total: ${total}")


acc1 = SavingsAccount("Ana", 500)
acc1.deposit(100)

acc2 = BusinessAccount("Tech Corp", 2000)
acc2.deposit(250)
