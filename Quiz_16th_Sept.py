# Using classes, Create a basic banking application with the following features:

# Create a class called BankAccount with the following attributes:
# account_number - a string
# balance - a float
# owner - a string
# type - a string
# Create a class called Bank with the following attributes:

# name - a string
# accounts - a list of BankAccount objects
# Create a class called Customer with the following attributes:

# name - a string
# accounts - a list of BankAccount objects
# Create a class called Transactions with the following attributes:

#  1. `account` - a `BankAccount` object
#  2. `amount` - a float
#  3. `type` - a string
# The application should have the following functionality:

# Create a new Bank object
# Create a new Customer object
# Create a new BankAccount object
# Add the BankAccount object to the Bank object
# Add the BankAccount object to the Customer object
# Print the Bank object
# Print the Customer object
# Print the BankAccount object
# Create a new Transaction object
# Add the Transaction object to the BankAccount object


# SOLUTIONS

# Creating a class called BankAccount
class BankAccount:
   def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

# Creating a class called Bank
class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

# Creating a class called Customer
class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accunts = accounts

# Creating a class called Transactions
class Transactions:
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type

# Creating a new Bank object
NewBank = Bank("Centenary Bank", (2013571841, 6729825901, 16342637241))

# Creating a new Customer object
New_Customer = Customer("Lawrence Ssettuba", (2013571841, 6729825901, 16342637241))

# Creating a new BankAccount object
NewBankAccount = BankAccount("7012359014", 5500000.100, "Lawrence Ssettuba", "Savings Account")

# Adding the BankAccount object to the Bank object
NewBankAccount = NewBank.accounts

# Adding the BankAccount object to the Customer object
NewBankAccount = New_Customer.name

# Printing the Bank object
print(f"Bank Name: {NewBank.name} \nAccounts: {NewBank.accounts}\n")

# Printing the Customer object
print(f"Customer Namer: {New_Customer.name}\nCustomer's Acounts: {New_Customer.accunts}\n")

# Printing the BankAccount object
print(f"Account Number: {NewBankAccount.account_number} \nAccount Owner: \
    {NewBankAccount.owner} \nBalance: {NewBankAccount.balance} \nType: {NewBankAccount.type}\n")

# Creating a new Transaction object  
NewTransaction = Transactions(2013571841, 1000000.0, "Withdrawing")  

# Adding the Transaction object to the BankAccount object
NewTransaction = BankAccount.NewBankAccount





      