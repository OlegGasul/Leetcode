class Bank:

    def __init__(self, balance):
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > len(self.balance):
            return False
        
        if account2 < 1 or account2 > len(self.balance):
            return False
        
        if self.balance[account1 - 1] < money:
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self.balance):
            return False
        
        self.balance[account - 1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self.balance):
            return False
        
        if self.balance[account - 1] < money:
            return False
        
        self.balance[account - 1] -= money
        return True

bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))