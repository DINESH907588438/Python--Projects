#ATM problem 
withdrawal_amount = int(input("Enter the withdrawal amount: "))
balance_amount = int(input("Enter the Balance amount: "))              
withdrawal_amount = int(withdrawal_amount)                        
balance_amount = float(balance_amount)
print("The Balance amount after the transaction: ")
if (withdrawal_amount % 5 == 0 and balance_amount>=(withdrawal_amount+0.5)):
    balance_amount = balance_amount - withdrawal_amount - 0.5     
    print(round(balance_amount,2))
else:
    print(round(balance_amount,2))
