'''
ATM withdrawal with exception handling
balance=100000
ip-> amount which needs to be taken
 
amount>0 if <=0 raise Error
amount>balance raise error
else print the message withdraw successful, remaining balance
'''
class InsufficientBalanceError(Exception):
    pass
balance= 100000
amount=int(input())
if(amount<=0):
    raise ValueError("Amount Value should be positive")
elif amount>balance:
    raise InsufficientBalanceError("Amount should within balance limit")
else:
    print("Successful! remaining balance is",balance-amount)