class Bank():
       def __init__(self, balance):
           self.balance = balance
   
       @staticmethod
       def find_interest(loan_money, interest_rate):
           return loan_money * (1 + interest_rate) * 299



bank = Bank(1000)
print(bank.find_interest(bank.balance, 0.3))


class ATM(Bank):
    def __init__(self, balance):
        super().__init__(balance)
     
    @staticmethod
    def find_interest(loan_money):
        return loan_money * 1.4
 
atm = ATM(1000)
print(ATM.find_interest(100))
print(atm.find_interest(atm.balance))