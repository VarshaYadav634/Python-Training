# class BankAccount:
#     def __init__(self,name,acc_no,balance):
#         self.n=name
#         self.acc_no=acc_no
#         self.balance=balance
#     def deposit(self,amt):
#         self.balance+=amt
#     def withdraw(self,amt):
#         if self.balance>=amt:
#             self.balance-=amt
#         else:
#             print("insufficient balance")
#     def account_summary(self):
#         print("name:",self.n)
#         print("acc_no:",self.acc_no)
#         print("current balance:",self.balance)
# a1=BankAccount("Ram",110,500)
# a1.deposit(500)
# a1.withdraw(200)
# a1.account_summary()
# a2=BankAccount("Gopal",220,800)
# a2.deposit(300)
# a2.withdraw(200)
# a2.account_summary()

#or

'''
task:Bank account management system
objective: use python classes to simuate basicbank account operations
 
task description: create a class called as BankAccount
 
the class should have:
1. constructor that accepts account holder name, account number, initial balance
2. a method deposit(amount)- adds amount to balance
3. a method withdraw(amount)- subtracts amount if balance is sufficient
4. a method display_balance()- prints current balance
5. a method account_summary() - prints name, account no and balance
'''
class bankaccount:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance=self.balance-amount
        else:
            print("insufficient balance")
    def display_balance(self):
        print("current balance is: ",self.balance)
    def account_summary(self):
        print("Account Holder Name: ",self.name)
        print("Account Number: ",self.acc_no)
        print("Account Balance: ",self.balance)
p1=bankaccount("Abc",37890,50000)
p1.deposit(10000)
p1.deposit(15000)
p1.withdraw(5000)
p1.display_balance()
p1.account_summary()




    



