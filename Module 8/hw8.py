"""Homework 8
HW8: Import Banking and instantiate two users with balances
HW8: User can withdraw
HW8: User can deposit
HW8: User can print balance
"""

# Import Banking and instantiate two users with balances
from banking import Banking

User1 = Banking("Dianna", 5000)
User2 = Banking("Greg", 100)

# User can withdraw
User1.withdrawal(300)

User2.withdrawal(200)

# User can deposit
User1.deposit(1000)
User2.deposit(1000)

# User can print balance
User1.print_balance()
User2.print_balance()
