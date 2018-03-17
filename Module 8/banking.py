"""Homework 8
Create a Banking class that does the following:
Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account
"""

# Create a Banking class
class Banking():

# Banking: Track initial account balance
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance
        print("Hi {}! Welcome to Tingg Bank. Your initial account balance is ${}.".format(user, "%.2f" % balance))

# Banking: Track deposits
    def deposit(self, deposit):
        self.balance += deposit
        print("Thank you for your deposit of ${}. Your current balance is ${}.".format("%.2f" % deposit, "%.2f" % self.balance))

# Banking: Track withdrawal
# Banking: Prints error if overdraft
    def withdrawal(self, withdrawal):
        if withdrawal > self.balance:
            print("Sorry, there are insufficient funds in your account to withdraw ${}. Your current balance is ${}.".format("%.2f" % withdrawal, "%.2f" % self.balance))
        else:
            self.balance -= withdrawal
            print("Thank you for your withdrawal of ${}. Your current balance is ${}.".format("%.2f" % withdrawal, "%.2f" % self.balance))

# Banking: Track and Print current balance
    def print_balance(self):
        print("Thank you for your inquiry. Your current balance is ${}.".format("%.2f" % self.balance))

