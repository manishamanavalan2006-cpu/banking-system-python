class Bank_Account:
    def __init__(self,account_no):
        self.account_no=account_no
        self.balance=0
        self.history_details=[]
    
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            self.history_details.append(f"Deposite {amount}")
        else:
            print("Invalid amount ")
    
    def withdraw(self,amount):
        if self.balance>=amount and amount>0:
            self.balance-=amount
            self.history_details.append(f"Withdraw {amount}")
        else:
            print("Insufficient balance")
    
    def amount_transfer(self,acc,amount):
        if self.balance>=amount and amount>0:
            self.withdraw(amount)
            acc.deposite(amount)
            self.history_details.append(f"Transfer {amount} to the Account No:  {acc.account_no}")
        else:
            print("Insufficient balance")

    def transaction_history(self):
        print("______________________________________")
        print(f"Account No: {self.account_no}, Current balance: {self.balance}")
        for i in self.history_details:
            print(i)
        
user1=Bank_Account("456883")
user2=Bank_Account("903473920")
user2.deposite(10000)
user1.deposite(5000)
user1.withdraw(250)
user2.withdraw(500)
user2.amount_transfer(user1, 2000)
user1.transaction_history()
user2.transaction_history()